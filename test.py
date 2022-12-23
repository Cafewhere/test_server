from flask import Flask, request, jsonify
import time, json
import returnJson


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'CafeWhere : Hello, World!'

@app.route('/test')
def get_test():
    return jsonify({"date": time.strftime('%Y-%m-%d', time.localtime(time.time()))})

@app.route('/api/req', methods=['POST'])
def print_res():
    return returnJson.getTest()

if __name__ == "__main__":
    app.run()
