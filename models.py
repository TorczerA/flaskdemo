from marshmallow import Schema, fields
from app import db


class UserTable(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)

    def __init__(self, data):
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')

    def create_user(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)

    def __repr__(self):
        return '<id {} : {} {}'.format(self.id, self.first_name, self.last_name)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)


class PostsTable(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(2000), nullable=True)

    def __init__(self, data):
        self.title = data.get('title')
        self.body = data.get('body')

    def create_post(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body
        }

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, post_id):
        return cls.query.get(post_id)

    def __repr__(self):
        return '<id {} : {} {}'.format(self.id, self.title, self.body)


class PostsSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
