Flask Internationalization (i18n) Project
This project demonstrates the implementation of internationalization (i18n) in a Flask web application using the Flask-Babel extension. The application includes several tasks that progressively introduce language support, user locale management, and timezone handling.

Requirements
Python 3.7+
Flask 2.x
Flask-Babel 2.x
pytz
pybabel (for managing translations)
Setup and Installation
1. Clone the repository:
bash
Copy code
git clone https://github.com/your_username/alx-backend.git
cd alx-backend/0x02-i18n
2. Create and activate a virtual environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install the required dependencies:
bash
Copy code
pip install flask flask_babel pytz
4. Extract and compile translations (if working with translations):
Make sure to extract strings and compile translations for the application:

bash
Copy code
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
pybabel compile -d translations
File Structure
bash
Copy code
/0x02-i18n
    ├── 0-app.py              # Basic Flask app with "Hello world" message
    ├── 1-app.py              # Flask app with Babel setup
    ├── 2-app.py              # Locale selection from request
    ├── 3-app.py              # Template internationalization
    ├── 4-app.py              # Locale selection via URL parameter
    ├── 5-app.py              # Mock user login and locale handling
    ├── 6-app.py              # User locale-based i18n
    ├── 7-app.py              # Timezone handling with pytz
    ├── app.py                # Final app with time display
    ├── babel.cfg             # Babel configuration file
    ├── translations/         # Folder for translation files (.po/.mo)
    │   ├── en/               # English translation folder
    │   │   └── LC_MESSAGES/messages.po
    │   └── fr/               # French translation folder
    │       └── LC_MESSAGES/messages.po
    ├── templates/            # HTML templates
    │   ├── 0-index.html      # Basic index template
    │   ├── 1-index.html      # Template for Babel setup
    │   ├── 2-index.html      # Template for locale-based display
    │   ├── 3-index.html      # Template for parametrized text
    │   ├── 4-index.html      # Template for URL-based locale
    │   ├── 5-index.html      # Template for mock user login
    │   ├── 6-index.html      # Template for user locale handling
    │   └── 7-index.html      # Template for timezone handling
    └── README.md             # Project documentation
Tasks Breakdown
Basic Flask App: Set up a basic Flask app with a single route that displays "Hello world!".
Babel Setup: Install and configure Flask-Babel to manage language settings for the app.
Locale from Request: Automatically determine the user’s preferred language based on the request headers.
Template Parametrization: Use the _() function to parametrize the text in the templates and make them translatable.
Locale via URL Parameter: Allow users to force a specific locale by adding a locale parameter to the URL.
Mock User Login: Simulate user login and provide personalized greetings based on the user's locale.
User Locale: Determine the user’s preferred locale from URL parameters or user settings.
Timezone Handling: Infer the user’s timezone and display the current time based on that timezone.
