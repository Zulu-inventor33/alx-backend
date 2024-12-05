#!/usr/bin/env python3
"""
Flask app that uses user locale preferences and language settings.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Create the Flask app
app = Flask(__name__)


# Set up Babel
class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

# Simulate a user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Returns a user dictionary based on URL parameter or None."""
    user_id = request.args.get('login_as')
    if user_id:
        user = users.get(int(user_id))
        return user
    return None


@app.before_request
def before_request():
    """Before request function to set the user globally."""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


def get_locale():
    """Determines the best match for the user's locale."""
    if g.user and g.user["locale"] in app.config['LANGUAGES']:
        return g.user["locale"]
    # Check if locale is passed via URL parameter
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Fall back to request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Home page route."""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
