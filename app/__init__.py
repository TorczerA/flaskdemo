from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig

flaskAppInstance = Flask(__name__)
flaskAppInstance.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app=flaskAppInstance)

__import__('app.api')