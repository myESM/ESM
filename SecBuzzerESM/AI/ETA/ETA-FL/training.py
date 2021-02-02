import datetime, os, configparser, pickle, pytz, shutil, json

import pandas as pd
import numpy as np

from elasticsearch import Elasticsearch, helpers
from xgboost.sklearn import XGBClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold


class Main():
  def __init__(self):
    config = configparser.ConfigParser()
    config.read(os.path.dirname(os.path.abspath(__file__))+"/config.ini")
    self.now = datetime.datetime.now(pytz.timezone("Asia/Taipei"))
    # es
    self.es_server = config.get("ES", "es_server")
    self.es_port = eval(config.get("ES", "es_port"))
    # train
    self.period = eval(config.get("Train", "period"))
    self.preds = eval(config.get("Train", "preds"))
    self.K = eval(config.get("Train", "K"))
    self.skfold = StratifiedKFold(n_splits=self.K, random_state=7, shuffle=True)
    self.N_Class = eval(config.get("Train", "N_Class"))
    self.label_table = eval(config.get("Train", "label_table"))
    self.model_path = os.path.dirname(os.path.abspath(__file__))+"/"+config.get("Train", "model_path")
  
  def esIdxList(self, es_index1):
    es_index_list = [es_index1+(self.now - datetime.timedelta(days=x+1)).strftime("%Y%m%d") for x in range(0,self.period)]
    es = Elasticsearch([{"host":self.es_server, "port":self.es_port}])
    es_index_exist = es.indices.get_alias(es_index1+"*").keys()
    index_list = list(set(es_index_list)&set(es_index_exist))
    return index_list

  def queryES1(self, es_index):
    es = Elasticsearch([{"host":self.es_server, "port":self.es_port}])
    # es_index_list = [es_index+(self.now - datetime.timedelta(days=x+1)).strftime("%Y%m%d") for x in range(0,self.period)]
    # es_index_exist = es.indices.get_alias(es_index+"*").keys()
    # index_list = list(set(es_index_list)&set(es_index_exist))
    # res = helpers.scan(client=es, scroll="10m", index=index_list)
    res = helpers.scan(client=es, scroll="10m", index=es_index)
    return res

  def queryES2(self, es_index):
    es = Elasticsearch([{"host":self.es_server, "port":self.es_port}])
    es_index_list = list(set([es_index+(self.now - datetime.timedelta(days=x+1)).strftime("%Y-%m") for x in range(0,self.period+30)]))
    es_index_exist = es.indices.get_alias().keys()
    index_list = list(set(es_index_list)&set(es_index_exist))
    res = helpers.scan(client=es, scroll="10m", index=index_list)
    return res

  def queryES3(self, es_index):
    es = Elasticsearch([{"host":self.es_server, "port":self.es_port}])
    res = helpers.scan(client=es, scroll="10m", index=es_index)
    return res

  def toEdgeDf(self, res):
    df = pd.DataFrame()
    data = list()
    for idx, nf in enumerate(res):
      if idx%1E4 == 0:
        df = pd.concat([df, pd.DataFrame(data)], axis=0)
        data = list()
      tmp = dict()
      tmp["id"] = nf["_id"]
      tmp.update(nf["_source"])
      data.append(tmp)
    df = pd.concat([df, pd.DataFrame(data)], axis=0)
    df["t0"] = df["First packet time"].astype("int").apply(lambda x: x/1E6)
    df["t1"] = df["Last packet time"].astype("int").apply(lambda x: x/1E6)
    def toProto(proto):
      tmp = str()
      if proto == 6:
        tmp = "TCP"
      elif proto == 17:
        tmp = "UDP"
      elif proto == 1:
        tmp = "ICMP"
      else:
        tmp = "UNKNOWN"
      return tmp
    df["proto"] = df["Protocol"].astype("int").apply(toProto)
    df = df.astype("str")
    return df

  def toAlertDf(self, res):
    df = pd.DataFrame()
    data = list()
    for idx, nf in enumerate(res):
      if idx%1E4 == 0:
        df = pd.concat([df, pd.DataFrame(data)], axis=0)
        data = list()
      tmp = dict()
      tmp["Src IP"] = nf["_source"]["src_ip"]
      tmp["Dst IP"] = nf["_source"]["dest_ip"]
      tmp["proto"] = nf["_source"]["proto"]
      tmp["timestamp"] = nf["_source"]["timestamp"]
      tmp["Src Port"] = nf["_source"].get("src_port", 99999)
      tmp["Dst Port"] = nf["_source"].get("dest_port", 99999)
      data.append(tmp)
    df = pd.concat([df, pd.DataFrame(data)], axis=0)
    def toEpochTime(t):
      tmp = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%f+0800")
      epoch = (tmp - datetime.datetime(1970, 1, 1)).total_seconds()
      return epoch
    try:
      df["t"] = df["timestamp"].apply(toEpochTime)
      df.drop("timestamp", axis=1, inplace=True)
      df = df.astype("str")
    except:
      pass
    return df

  def toMalDf(self, res):
    data = list()
    for nf in res:
      tmp = dict()
      tmp["id"] = nf["_id"]
      tmp.update(nf["_source"])
      data.append(tmp)
    df = pd.DataFrame(data)[self.preds + ["class", "Payload BYTE Distribution"]]
    return df

  def filterBenign(self, edge, label):
    df0 = pd.merge(edge, label, on=["Src IP","Src Port","Dst IP","Dst Port","proto"], how="left")
    c1 = df0.groupby("id").size().reset_index(name="c1")
    df1 = pd.merge(df0, c1)
    del df0, c1
    df1["t0"] = df1["t0"].astype("float")
    df1["t1"] = df1["t1"].astype("float")
    df1["t"] = df1["t"].astype("float")
    df1["inlb"] = df1["t"] >= df1["t0"]
    df1["inub"] = df1["t"] <= df1["t1"]
    df1["in"] = df1["inlb"] & df1["inub"]
    df2 = df1[~df1["in"]]
    del df1
    c2 = df2.groupby("id").size().reset_index(name="c2")
    df3 = pd.merge(df2, c2)
    del df2, c2
    df4 = df3[df3["c1"] == df3["c2"]]
    del df3
    df5 = df4.drop(["proto","in","inlb","inub","t0","t1","t","c1","c2"], axis=1)
    del df4
    df5 = df5.drop_duplicates()
    df5["class"] = "normal"
    df5 = df5[self.preds + ["class", "Payload BYTE Distribution"]]
    return df5

  def processData(self, benign, malware):
    df = pd.concat([benign, malware], axis=0)
    def mapping(m):
      encode = int()
      for k, v in self.label_table.items():
        if m == v:
          encode = k
          break
      return encode
    y = df["class"].apply(mapping).values
    df.drop("class", axis=1, inplace=True)
    # 42+256 features and rename columns
    cols_bytes = ["byte_{}".format(i) for i in range(256)]
    df[cols_bytes] = df["Payload BYTE Distribution"].str.split("-", expand=True)
    df = df[self.preds+cols_bytes].astype("float")
    df.replace(np.inf, 1E6, inplace=True) # 2, Flow Bytes/s, Flow Packets/s
    df.fillna(0, inplace=True) # 9, Fwd b_p BCD Min, Fwd b_p BCD Max, Fwd b_p BCD Mean, Fwd b_p BCD Std, Bwd b_p BCD Min, Bwd b_p BCD Max, Bwd b_p BCD Mean, Bwd b_p BCD Std, Flow Bytes/s
    # df = df.values
    return df, y

  def paraGridSearch(self, X, y):
    if os.path.exists(self.model_path+"bast_params.json"):
      with open(self.model_path+"bast_params.json") as f:
        best_params = json.load(f)
    else:
      X = X.copy()
      parameters = {"nthread":[4],
                    "objective":["multi:softmax"],
                    "learning_rate": [0.05],
                    "max_depth": [2],
                    "min_child_weight": [3],
                    "gamma": [0.1],
                    "subsample": [0.8],
                    "colsample_bytree": [0.7],
                    "n_estimators": [10],
                    # "tree_method": ["gpu_hist"],
                    "seed": [1337]}
      # stratify sampling
      NUM_SAMPLE = 1E5
      X["class"] = y
      X = X.groupby("class", group_keys=False).apply(lambda x: x.sample(int(np.rint(NUM_SAMPLE*len(x)/len(X))))).sample(frac=1).reset_index(drop=True)
      y = X["class"].values
      X.drop("class", axis=1, inplace=True)
      xgb_model = XGBClassifier()
      clf = GridSearchCV(xgb_model, parameters, n_jobs=5, cv=self.skfold, scoring="f1_micro", verbose=1, refit=True)
      clf.fit(X.values, y)
      best_params = clf.best_params_
      with open(self.model_path+"bast_params.json", "wb") as f:
        f.write(json.dumps(best_params).encode("utf-8"))
        f.close()
    return best_params

  def initialEnv(self):
    if os.path.exists(self.model_path):
      try:
        shutil.rmtree(os.path.dirname(os.path.abspath(__file__))+"/previous_model/")
      except:
        pass
      os.rename(self.model_path, os.path.dirname(os.path.abspath(__file__))+"/previous_model/")
    os.mkdir(self.model_path)
    np.random.seed(1314)

  def model(self, best_params, X, y, fmp=False, save=False):
    clf_best = XGBClassifier(learning_rate=best_params["learning_rate"],\
                             n_estimators=best_params["n_estimators"],\
                             max_depth=best_params["max_depth"],\
                             min_child_weight=best_params["min_child_weight"],\
                             gamma=best_params["gamma"],\
                             subsample=best_params["subsample"],\
                             colsample_bytree=best_params["colsample_bytree"],\
                             objective=best_params["objective"],\
                             nthread=best_params["nthread"],\
                             seed=best_params["seed"],\
                            #  tree_method=best_params["tree_method"],\
                             num_class = self.N_Class)
    # oof = np.zeros([len(X), self.N_Class])
    df_fmp = np.zeros((self.K, X.shape[1]))
    for fold_, (train_index, valid_index) in enumerate(self.skfold.split(X.values, y)):
      try:
        m_path = self.model_path + "000{}.model.pickle.dat".format(fold_)
        m = pickle.load(open(m_path, "rb"))
        m.save_model(self.model_path + "000{}.model".format(fold_))
        model = self.model_path + "000{}.model".format(fold_)
      except:
        model = None
      train_X, valid_X = X.values[train_index], X.values[valid_index]
      train_y, valid_y = y[train_index], y[valid_index]
      estimator = clf_best.fit(train_X, train_y, eval_set=[(valid_X, valid_y)], verbose=5, xgb_model=model, early_stopping_rounds=100)
      if save == True:
        pickle.dump(estimator, open(self.model_path+"000{}.model.pickle.dat".format(fold_), "wb"))
        if model != None:
          os.remove(self.model_path + "000{}.model".format(fold_))
      # oof[valid_index] = estimator.predict_proba(valid_X)
      df_fmp[fold_] = estimator.feature_importances_
    if fmp == True:
      return df_fmp

  def featureSelect(self, fmp):
    df_fmp = pd.DataFrame(fmp, columns=self.preds+["byte_{}".format(i) for i in range(256)])
    fmp_mean = df_fmp.mean()
    THRESHOLD = 0
    preds_sel = fmp_mean[fmp_mean > THRESHOLD].index.tolist()
    with open(self.model_path+"preds_sel.txt", "w") as text_file:
      text_file.write(str(preds_sel))
    return preds_sel

if __name__ == "__main__":
  load_main = Main()
  es_index1 = "cic-"
  es_index2 = "suricata-"
  es_index3 = "malware-20201020"
  #
  best_params = None
  preds_sel = None
  load_main.initialEnv()
  res2 = load_main.queryES2(es_index2)
  label = load_main.toAlertDf(res2)
  res3 = load_main.queryES3(es_index3)
  malware = load_main.toMalDf(res3)
  for idx1 in load_main.esIdxList(es_index1):
    res1 = load_main.queryES1(idx1)
    edge = load_main.toEdgeDf(res1)
    if len(label) != 0:
      benign = load_main.filterBenign(edge, label)
    else:
      benign = edge.copy()
    X, y = load_main.processData(benign, malware)
    if best_params == None:
      best_params = load_main.paraGridSearch(X, y)
    if preds_sel == None:
      fmp = load_main.model(best_params, X, y, fmp=True)
      preds_sel = load_main.featureSelect(fmp)
    X = X[preds_sel]
    load_main.model(best_params, X, y, save=True)