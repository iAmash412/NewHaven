from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from controllers import cats
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def landing_page():
    return render_template("landing_page.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
