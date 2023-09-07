#!/usr/bin/python3
"""Import a Flask web application"""
from flask import Flask

app = Flask(__name__)


app.route('/', strict_slashes=False)


def hello_hbnb():
    """Print Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port='5000')
