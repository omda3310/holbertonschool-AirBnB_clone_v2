#!/usr/bin/python3
"""Import a Flask web application"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hbnb_python(text="is cool"):
    """show text"""
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def hbnb_number(n):
    """show number"""
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def hbnb_template5(n):
    """show number"""
    return(render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hbnb_odd_even(n):
    "the number is even or odd"
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000')
