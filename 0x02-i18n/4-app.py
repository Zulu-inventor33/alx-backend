#!/usr/bin/env python3
"""
Flask application with forced locale via URL parameter.
"""

from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """
    Determines the best match for supported
    languages based on the request or URL parameters.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route that renders the index.html template with internationalized content.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()