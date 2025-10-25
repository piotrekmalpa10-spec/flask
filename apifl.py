import flask
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
data = []

@app.route("/posts", methods=["POST"])
def dodaj():
    payload = request.get_json()
    new_data = {"title": payload['passwo'], "author": payload['username']}
    data.append(new_data)
    return jsonify(new_data), 201



@app.route("/posts", methods=["GET"])
def dodwfaj():
    return jsonify(data)

if __name__ == '__main__': app.run()


