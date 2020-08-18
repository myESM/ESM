# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from elasticsearch import Elasticsearch


class ElasticsearchConnector():
  def __init__(self, ES_HOST, ES_PORT):
    self.es_host = ES_HOST
    self.es_port = ES_PORT
    self.es = Elasticsearch([{"host" : self.es_host, "port" : self.es_port}])
    logging.info("Create the Elasticsearch Connector: {0}".format(ES_HOST))

  def insert_result(self, es_index, result_object):
    if self.es.indices.exists(index=es_index) == False:
      self.es.indices.create(index=es_index)
      logging.info("Create the Elasticsearch index: {0}".format(es_index))
    try:
      result_object["ingest_timestamp"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
      self.es.index(index=es_index, body=result_object)
    except Exception as e:
      logging.error("Elasticsearch insert error: {0}".format(e))
