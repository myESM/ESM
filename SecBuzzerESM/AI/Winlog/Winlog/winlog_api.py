#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from flask import Flask, jsonify, make_response, request
from winlog_rule_based import winlog_rule_based

app = Flask(__name__)

# 404 message for bad requests
@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({"error": "404 NOT FOUND"}), 404)

# 500 message for bad requests
@app.errorhandler(500)
def not_found(error):
  return make_response(jsonify({"error": "500 INTERNAL SERVER ERROR"}), 500)

# run winlog api
@app.route("/winlog/api/v1.0", methods=["GET"])
def winlog_handler():
  #check the parameters
  es_index = request.args.get("index", None)
  es_start_time = request.args.get("start_time", None)
  es_end_time = request.args.get("end_time", None)
  if es_index == None or es_start_time == None or es_end_time == None:
    missing_parameter = ""
    if es_index == None:
      missing_parameter += " {es_index} "
    if es_start_time == None:
      missing_parameter += " {es_start_time} "
    if es_end_time == None:
      missing_parameter += " {es_end_time} "
    return jsonify({"error": "Missing parameter" + missing_parameter})
  else:
    winlog_rule_based(es_index, es_start_time, es_end_time)
    return jsonify({"result": "Done"})

app.run(host="0.0.0.0", port=5000, debug=False)
