import datetime
import configparser, pickle, json
import pandas as pd
import numpy as np

from elasticsearch import Elasticsearch, helpers


class Main():
  def __init__(self):
    config = configparser.ConfigParser()
    config.read("config.ini")
    # es
    self.es_server = config.get("ES", "es_server")
    self.es_port = eval(config.get("ES", "es_port"))
    # model
    self.K = eval(config.get("Model", "K"))
    self.N_Class = eval(config.get("Model", "N_Class"))
    self.model_path = config.get("Model", "model_path")
    self.m0 = config.get("Model", "m0")
    self.m1 = config.get("Model", "m1")
    self.m2 = config.get("Model", "m2")
    self.m3 = config.get("Model", "m3")
    self.m4 = config.get("Model", "m4")
    self.preds = eval(config.get("Model", "preds"))
    self.attck_table = eval(config.get("Model", "attck_table"))
    self.attck_msg = eval(config.get("Model", "attck_msg"))
    self.proto_table = eval(config.get("Model", "proto_table"))
    self.sig_id = eval(config.get("Model", "sig_id"))
    self.url_table = eval(config.get("Model", "url_table"))

  def queryES(self, es_index, start_time, end_time):
    es = Elasticsearch([{"host":self.es_server, "port":self.es_port}])
    print("start_time:", start_time)
    print("end_time:", end_time)
    body = {"query":{"bool":{"must":[{"range":{"Timestamp":{"gt":start_time,"lt":end_time}}}]}}}
    res = helpers.scan(client=es, scroll="2m", query=body, index=es_index)
    print("es_index:", es_index)
    return res
  
  def toDf(self, res):
    data = list()
    for nf in res:
      tmp = dict()
      tmp["id"] = nf["_id"]
      tmp.update(nf["_source"])
      data.append(tmp)
    df = pd.DataFrame(data)
    return df
  
  def processData(self, df):
    # 67 features and rename columns
    df_fin = df[self.preds]
    df_id = df[["id", "Timestamp", "Src IP", "Src Port", "Dst IP", "Dst Port", "Protocol", "nic_name"]]
    return df_fin, df_id
  
  def predict(self, df):
    m0 = pickle.load(open(self.model_path+self.m0, "rb"))
    m1 = pickle.load(open(self.model_path+self.m1, "rb"))
    m2 = pickle.load(open(self.model_path+self.m2, "rb"))
    m3 = pickle.load(open(self.model_path+self.m3, "rb"))
    m4 = pickle.load(open(self.model_path+self.m4, "rb"))
    predictions = np.zeros([self.K, len(df), self.N_Class])
    # predict
    predictions[0] = m0.predict_proba(df.values)
    predictions[1] = m1.predict_proba(df.values)
    predictions[2] = m2.predict_proba(df.values)
    predictions[3] = m3.predict_proba(df.values)
    predictions[4] = m4.predict_proba(df.values)
    #average
    pred = np.argmax(predictions.mean(axis=0), axis=1)
    return pred

  def toJSON(self, pred, df_id):
    df = df_id.copy()
    # rename
    df.rename(columns={"id":"flow_id",
                       "Timestamp":"log_time",
                       "Src IP":"src_ip",
                       "Src Port":"src_port",
                       "Dst IP":"dest_ip",
                       "Dst Port":"dest_port",
                       "Protocol":"proto",
                       "nic_name":"in_iface"}, inplace=True)
    df["src_port"] = df["src_port"].astype("int")
    df["dest_port"] = df["dest_port"].astype("int")
    df["proto"] = df["proto"].apply(lambda x: self.proto_table[x])
    df["title"] = [self.attck_table[x] for x in pred] # alert.category
    t = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f+08:00") 
    df["timestamp"] = t 
    df["event_type"] = "alert"
    df["severity"] = 2 # alert.severity
    df["message"] = df["title"].apply(lambda x: self.attck_msg[x]) # alert.signature
    df["action"] = "" # alert.action
    df["rule_sig_id"] = df["title"].apply(lambda x: self.sig_id[x]) # alert.signature_id
    df["alert_group_id"] = 0 # alert.gid
    df["alert"] = df.apply(lambda x: {"category":x["title"], "severity":x["severity"], "signature":x["message"],
                                      "action":x["action"], "signature_id":x["rule_sig_id"], "gid":x["alert_group_id"]}, axis=1)
    df["reference"] = df["title"].apply(lambda x: self.url_table[x])
    df.drop(["title", "severity", "message", "action", "rule_sig_id", "alert_group_id"], axis=1, inplace=True)
    df["module"] = "ETA-ATTACK"
    df["log_type"] = "Traffic"
    df["dump_status"] = "0"
    df["ingest_timestamp"] = datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    output = eval(df.to_json(orient="records"))
    return output
  
  def toES(self, dic):
    count = 0
    es_idx = datetime.datetime.now().strftime("eta-attack-%Y-%m")
    for d in dic:
      if d["alert"]["category"] == "Benign":
        pass
      else:
        count += 1
        es = Elasticsearch([{"host":self.es_server, "port":self.es_port}])
        es.index(index=es_idx, doc_type="_doc", body=d)
    print("{} NetFlows are anomaly and save to ES".format(count))


if __name__ == "__main__":
  es_index = "cic_20200804"
  start_time = "2020-08-04T11:25:00.000000+08:00"
  end_time = "2020-08-04T11:30:00.000000+08:00"

  load_main = Main()
  res = load_main.queryES(es_index, start_time, end_time)
  df = load_main.toDf(res)
  if df.shape[0] != 0:
    df_fin, df_id = load_main.processData(df)
    pred = load_main.predict(df_fin)
    output = load_main.toJSON(pred, df_id)
    load_main.toES(output)
    print("[DONE]")
  else:
    print("[MSG] There is no data")