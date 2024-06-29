#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def home():
    """Displays 'Hello HBNB!'."""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>')
def show_c_text(text):
    """Displays 'C' followed by the value of <text>, with underscores replaced by spaces."""
    text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def show_python_text(text):
    """Displays 'Python' followed by the value of <text>, with underscores replaced by spaces."""
    text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>')
def show_number(n):
    """Displays '<n> is a number' only if <n> is an integer."""
    return f'{n} is a number'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
