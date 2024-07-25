#!/usr/bin/python3
from flask import Flask
"""Flask web application module."""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Route handler for the root URL. returns Hello HBNB!$"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
