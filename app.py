from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging as logger
logger.basicConfig(level="DEBUG")

flaskAppInstance = Flask(__name__)
flaskAppInstance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
flaskAppInstance.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
    DB_USER="postgres", DB_PASS="embibe", DB_ADDR="localhost:5432", DB_NAME="demodb")
db = SQLAlchemy(app=flaskAppInstance)

from models import *

if __name__ == "__main__":
    logger.debug("----------------------------------------------------------------------------Starting the application")
    # noinspection PyUnresolvedReferences
    from api import *
    flaskAppInstance.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
