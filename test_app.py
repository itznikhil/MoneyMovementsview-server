from flask import Flask, jsonify, request
from data import data
# initialize our Flask application
app = Flask(__name__)


@app.route("/moneymovements", methods=["GET"])
def money_movements():
    return jsonify(data), 200


#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(debug=True)
