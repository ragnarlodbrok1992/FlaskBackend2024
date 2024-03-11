from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"


# @app.route("/hello/<name>")
# def hello(name):
#     return f"<p>Hello, {escape(name)}!</p>"

# Rendering templates

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template(['hello.html'],
                           name=name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    print(post_id)
    print(type(post_id))
    return f"<p>Post with id {escape(post_id)}</p>"


@app.route('/post/<post_id>')
def show_post_incorrect(post_id):
    return f"<p>Use number for post, not {escape(post_id)}!"
