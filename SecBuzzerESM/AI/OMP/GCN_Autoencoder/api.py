import logging

from flask import Flask, jsonify, make_response, request
import main

app = Flask(__name__)

# 404 message for bad requests
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "404 NOT FOUND"}), 404)

# 500 message for bad requests
@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({"error": "500 INTERNAL SERVER ERROR"}), 500)

# run eta1 api
@app.route("/omp_gcn/api/v1.0", methods=["GET"])
def omp_handler():
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
        load_main = main.Main()
        rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list, rel_test, feature_test, rel_normal, feature_normal, test_df, nic_name = load_main.loadES(es_index, es_start_time, es_end_time)
        normal_ip_list = load_main.oneModeProjection(rel_train_dict, rel_test_dict, feature_train_mat, feature_test_mat, ip_list)
        load_main.outputData(rel_test, feature_test, rel_normal, feature_normal, normal_ip_list, ip_list, test_df, es_start_time, es_end_time, nic_name)
        return jsonify({"result": "Done"})

app.run(host="0.0.0.0", port=5000, debug=False)

