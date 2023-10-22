#!/usr/bin/python3
"""script that starts a Flask web application
"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State

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


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Display number if it's a number
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a html template if the input is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a html template if the input is an integer
    """
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page of the States
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database again at the end of the request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
