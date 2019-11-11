class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'asdasdasd'
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:embibe@localhost/flaskdemo_db"


class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER="postgres", DB_PASS="embibe", DB_ADDR="localhost:5432", DB_NAME="demodb")
    DEVELOPMENT = True
    DEBUG = True
