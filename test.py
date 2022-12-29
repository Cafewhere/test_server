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

@app.route('/api/test', methods=['POST'])
def print_msg():
    foo = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "간단한 텍스트 요소입니다."
                    }
                }
            ]
        }
    }
    return json.dumps(foo)

if __name__ == "__main__":
    app.run()
