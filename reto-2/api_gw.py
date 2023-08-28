from flask import Flask, jsonify, request
import grpc_connection

app = Flask(__name__)
conn = grpc_connection.grpc_connection()

@app.route('/search_products', methods=['GET'])
def search_products():
    file_name = request.args.get('file_name')
    files = conn.search_products(file_name)
    return jsonify({"files": str(files)})

@app.route('/list_products', methods=['GET'])
def list_products():
    files = conn.list_products()
    return jsonify({"files": files})

if __name__ == "__main__":
    app.run(debug=True)