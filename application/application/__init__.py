from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_COOKIE_SECURE'] = True # set HttpOnly in session
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DATABASE.db'
db = SQLAlchemy(app)

from application.views import auth
from application.views import board
import application.database
