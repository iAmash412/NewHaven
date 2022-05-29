from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import cats
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
