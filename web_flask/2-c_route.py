#!/usr/bin/python3
"""
   Flask web application
   host: 0.0.0.0
   Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'c' then value of 'text' variable
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
        This function returns a passed in variable 'text'
        if it finds any '_' in 'text' it turns it to space ' '
    """
    Text = ""
    for i in range(len(text)):
        if text[i] == '_':
            Text += " "
        else:
            Text += text[i]

    return f'C {Text}'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
