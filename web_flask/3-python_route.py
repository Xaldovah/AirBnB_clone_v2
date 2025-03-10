#!/usr/bin/python3
"""script that starts a Flask web application
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Display 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display 'C is fun or any other c text'
    """
    return "C " + escape(text).replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Display 'Python is cool or any other c text'
    """
    return "Python " + escape(text).replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
