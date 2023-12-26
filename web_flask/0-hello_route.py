#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

"""
    A route to to return a function
"""


@app.route('/', strict_slashes=False)
def hello():
    """
        This function returns 'Hello world'
    """
    return 'Hello HBNB!\n'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
