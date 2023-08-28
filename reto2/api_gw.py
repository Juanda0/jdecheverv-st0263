from flask import Flask, jsonify, request
import grpc_connection
from configs import *
from producer import RunAMQP

app = Flask(__name__)
conn = grpc_connection.grpc_connection()

@app.route('/search_files', methods=['GET'])
def search_files():
    file_name = request.args.get('file_name')
    try:
        files = conn.search_files(file_name)
        print("Retrieved by GRCP")
    except:
        files = RunAMQP(file_name, function="search_files")
        print("Retrieved by AMQP")
    return jsonify(files)

@app.route('/list_files', methods=['GET'])
def list_files():
    try:
        files = conn.list_files()
        print("Retrieved by GRCP")
    except:
        files = RunAMQP("", function="list_files")
        print("Retrieved by AMQP")

    return jsonify(files)

if __name__ == "__main__":
    app.run(debug=True, host = API_GW_HOST, port = API_GW_PORT)