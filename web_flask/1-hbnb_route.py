#!/usr/bin/python3
"""
   Flask web application
   host: 0.0.0.0
   Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
        This function returns 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        This function returns 'HBNB'
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
