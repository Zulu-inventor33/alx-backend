#!/usr/bin/env python3
"""
Flask application with Babel setup for handling internationalization (i18n).
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Config class to setup available languages and default settings.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """
    Route that renders the index.html template with internationalized content.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
