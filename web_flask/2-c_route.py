#!/usr/bin/python3
"""
a script that starts a Flask web application
"""

from flask import Flask
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
def cisfun(text):
    """
    web application must be listening on 0.0.0.0, port 5000
    Routes:
    /c/<text>: display “C ” followed by the value of the text variable,
    (replace underscore _ symbols with a space )
    using the option strict_slashes=False in your route definition
    """
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
