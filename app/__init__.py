from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Create the Flask application instance
app = Flask(__name__, static_folder='static', template_folder='templates')

# Configure the app using the 'config.py' file
app.config.from_object('config')

# Initialize the database
db = SQLAlchemy(app)

# Import your views to register them with the app
from app import views

# Ensure the 'static' and 'templates' folders are configured
app._static_folder = 'static'
app._template_folder = 'templates'

if __name__ == '__main__':
    app.run(debug=True)
