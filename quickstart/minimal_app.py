"""
Minimal flask app
Runs with:
$ flask --app quickstart/minimal_app run
"""

from flask import Flask
from markupsafe import escape

# Flask instance is an WSGI app
app = Flask(__name__)


@app.route('/')  # tells flask what url triggers the function
def hello_world():
    """Hello world route"""
    return "<p>Hello, world!</p>"


@app.route('/<name>')
def hello(name: str):
    """Example variable url"""
    return f"<p>Hello, {escape(name)}</p>"


@app.route('/user/<string:username>')
def user_profile(username: str):
    """User profile page"""
    return f"<p>User: {escape(username)}</p>"


@app.route('/post/<int:post_id>')
def post_detail(post_id: int):
    """Post page"""
    return f"<p>Post id: {escape(post_id)}</p>"

# <converter:variable_name> variable converter types:
# string, int, float, path (string but also accepts slashes), uuid
