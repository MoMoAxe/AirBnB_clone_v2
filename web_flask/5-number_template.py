#!/usr/bin/python3
"""
   Flask web application
   host: 0.0.0.0
   Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays 'c' then value of 'text' variable
    /python/<text>: Displays 'Python' then value of 'text' variable
    /number/<n>: Displays '{n} is a number'
    /number_template/<n>: Displays a number passed in in a html life
"""

from flask import Flask, abort, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
        This function returns 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        This function returns 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """
        This function returns a passed in variable 'text'
        if it finds any '_' in 'text' it turns it to space ' '

         Returns: 'C {text}'
    """
    Text = ""
    for i in range(len(text)):
        if text[i] == '_':
            Text += " "
        else:
            Text += text[i]

    return f'C {Text}'


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """
        This function returns a passed in variable 'text'
        if it finds any '_' in 'text' it turns it to space ' '

        Returns: 'python {text}'
    """
    Text = ""
    for i in range(len(text)):
        if text[i] == '_':
            Text += " "
        else:
            Text += text[i]

    return f'Python {Text}' if text != "cool" else f'Python {text}'


@app.route('/number/<n>')
def number_n(n):
    """
        This function returns a passed in variable 'n'

         Returns: '{n} is a number'
    """

    try:
        n = int(n)
        return f'{n} is a number'
    except Exception:
        abort(404)


@app.route('/number_template/<n>')
def number_template(n):
    """
        This function returns a passed in variable 'n'

         Returns: n into an HTML file and displays it
    """

    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except Exception:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
