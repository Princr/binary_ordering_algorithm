from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


lm = LoginManager()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
# app.config['SECRET_KEY'] = "ime2019"
app.config.update(
    SECRETE_KEY = 'ime2019',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

lm.init_app(app)
migrate = Migrate(app, db)

from ime import models
from .views import *