#!/usr/bin/env python3
"""
Flask app with mock user login functionality and user-specific locale settings.
"""

from flask import Flask, render_template, request, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Returns a user dictionary based on the login_as URL parameter.
    """
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """
    Before each request, set the global
    user object based on the logged-in user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determines the best match for supported
    languages based on the user settings or request.
    """
    if g.user and g.user['locale']:
        return g.user['locale']


return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route that renders the index.html template with internationalized content.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
