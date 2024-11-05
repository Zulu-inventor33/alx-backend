#!/usr/bin/env python3
"""
Basic Flask application that displays "Hello world!" as the page header.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route that renders the index.html template with a simple message.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
