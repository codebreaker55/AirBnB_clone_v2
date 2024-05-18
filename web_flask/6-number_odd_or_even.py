#!/usr/bin/python3
"""
a script that starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
     web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    using the option strict_slashes=False in your route definition
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /hbnb: display “HBNB"
    using the option strict_slashes=False in your route definition
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /c/<text>: display “C ”, followed by the value of the text variable,
    (replace underscore _ symbols with a space)
    using the option strict_slashes=False in your route definition
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /python/<text>: display “Python ”, followed by the value of the,
    text variable(replace underscore _ symbols with a space),
    The default value of text is "is cool"
    using the option strict_slashes=False in your route definition
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def strict_number(n):
    """
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /number/<n>: display “n is a number” only if n is an integer
    using the option strict_slashes=False in your route definition
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def strict_numbers_templates(n):
    """
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /number_template/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    using the option strict_slashes=False in your route definition
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def strict_numbers_odd_even(n):
    """
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    using the option strict_slashes=False in your route definition
    """
    if n % 2 == 0:
        number_descrip = 'even'
    else:
        number_descrip = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           number_descrip=number_descrip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
