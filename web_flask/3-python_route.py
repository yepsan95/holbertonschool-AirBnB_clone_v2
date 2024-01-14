#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Access the root directory"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Access the /hbnb directory"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Access the /c<text> directory"""
    text = text.replace("_", " ")
    return f"C {text}"

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Access the /pyhton/<text> directory"""
    text = text.replace("_", " ")
    return f"Python {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)