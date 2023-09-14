#!/usr/bin/python3
"""Import a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB!"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print HBNB!"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hbnb_space(text):
    """show text"""
    text = text.replace("_", " ")
    return ("C {}".format(text))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000')
