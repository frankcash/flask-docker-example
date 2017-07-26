from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def helloWorld():
    resp = {
        "message": "flask is running"
    }
    return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
