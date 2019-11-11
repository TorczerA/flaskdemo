from app import db
from datetime import datetime


class PostsTable(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(2000), nullable=True)
    creation_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, data):
        self.title = data.get('title')
        self.body = data.get('body')
        self.creation_time = datetime.utcnow()
        self.user_id = data.get('user_id')

    @property
    def get_id(self):
        return self.id

    @property
    def get_user_id(self):
        return self.user_id

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
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.get_id,
            "title": self.get_title,
            "body": self.get_body,
            "creation_datetime": self.get_creation_time.__str__(),
            "user_id": self.get_user_id
        }

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()

    def __repr__(self):
        return '<id {} : {} {}'.format(self.id, self.title, self.body)

