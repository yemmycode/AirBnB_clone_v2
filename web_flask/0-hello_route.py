#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET'])  
def home():
    """
    Displays 'Hello HBNB!'.
    """
    return 'Hello HBNB!'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
