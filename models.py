from datetime import datetime
from app import db
import logging as logger


class UserTable(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)

    # USER AUTHENTICATION FIELDS
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # USER FIELDS
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean())

    posts = db.relationship('PostsTable', backref='users', lazy=True)

    def __init__(self, data):
        logger.debug('------------------------------------------------'
                     '----------------------------Initializing User Object')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.password = data.get('password')
        self.is_active = False
        logger.debug('----------------------------------------------------'
                     '------------------------Initialized User Object')

    @property
    def get_id(self):
        return self.id

    @property
    def get_email(self):
        return self.email

    @property
    def get_password(self):
        return self.password

    @property
    def get_first_name(self):
        return self.first_name

    @property
    def get_last_name(self):
        return self.last_name

    @property
    def get_is_active(self):
        return self.is_active

    def create_user(self):
        logger.debug('----------------------------------------------'
                     '------------------------------Creating User in Database')
        db.session.add(self)
        db.session.commit()
        logger.debug('-----------------------------------------------'
                     '-----------------------------Created User in Database')

    def update(self, data):
        logger.debug('------------------------------------------------'
                     '----------------------------Updating User in Database')
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
        logger.debug('--------------------------------------------------'
                     '--------------------------Updated User in Database')

    def serialize(self):
        return {
            "id": self.get_id,
            "first_name": self.get_first_name,
            "last_name": self.get_last_name,
            "email": self.get_email,
            "is_active": self.get_is_active,
        }

    def delete_user(self):
        logger.debug('-----------------------------------------------------'
                     '-----------------------Deleting User from Database')
        db.session.delete(self)
        db.session.commit()
        logger.debug('------------------------------------------------------'
                     '----------------------Deleted User from Database')

    @staticmethod
    def get_all_users():
        logger.debug('---------------------------------------------------'
                     '-------------------------Picking Up ALL Users from Database')
        return UserTable.query.all()

    @classmethod
    def get_by_id(cls, user_id):
        logger.debug('----------------------------------------------------'
                     '------------------------Picking Up Specified User from Database')
        return cls.query.get(user_id)

    def __repr__(self):
        return '<id {} : {} {}'.format(self.id, self.first_name, self.last_name)


class PostsTable(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(2000), nullable=True)
    creation_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, data):
        logger.debug('----------------------------------------------------'
                     '------------------------Initializing Post Object')
        self.title = data.get('title')
        self.body = data.get('body')
        self.creation_time = datetime.utcnow()
        self.user_id = data.get('user_id')
        logger.debug('----------------------------------------------------'
                     '------------------------Initialized Post Object')

    @property
    def get_id(self):
        return self.id

    @property
    def get_title(self):
        return self.title

    @property
    def get_body(self):
        return self.body

    @property
    def get_creation_time(self):
        return self.creation_time

    def create_post(self):
        logger.debug('---------------------------------------------'
                     '-------------------------------Creating Post in Database')
        db.session.add(self)
        db.session.commit()
        logger.debug('----------------------------------------------'
                     '------------------------------Created Post in Database')

    def update(self, data):
        logger.debug('----------------------------------------------'
                     '------------------------------Updating Post in Database')
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
        logger.debug('-----------------------------------------------'
                     '-----------------------------Updated Post in Database')

    def serialize(self):
        return {
            "id": self.get_id,
            "title": self.get_title,
            "body": self.get_body,
            "creation_datetime": self.get_creation_time.__str__(),
            "user_id": self.user_id
        }

    def delete_post(self):
        logger.debug('--------------------------------------------------'
                     '--------------------------Deleting Post from Database')
        db.session.delete(self)
        db.session.commit()
        logger.debug('---------------------------------------------------'
                     '-------------------------Deleted Post from Database')

    @classmethod
    def get_all_posts(cls):
        logger.debug('----------------------------------------------------'
                     '------------------------Picking Up ALL Posts from Database')
        return cls.query.all()

    @classmethod
    def get_post_by_user_id(cls, user_id):
        logger.debug('--------------------------------------------------'
                     '--------------------------Picking Up Posts for Specified User from Database')
        return cls.query.get(user_id)

    @classmethod
    def get_by_id(cls, post_id):
        logger.debug('----------------------------------------------------'
                     '------------------------Picking Up Specified Post from Database')
        return cls.query.get(post_id)

    def __repr__(self):
        return '<id {} : {} {}'.format(self.id, self.title, self.body)
