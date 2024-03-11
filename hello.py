from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"


@app.route("/hello/<name>")
def hello(name):
    return f"<p>Hello, {escape(name)}!</p>"
