from app import db


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
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.email = data.get('email')
        self.password = data.get('password')
        self.is_active = False

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
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.get_id,
            "first_name": self.get_first_name,
            "last_name": self.get_last_name,
            "email": self.get_email,
            "is_active": self.get_is_active,
        }

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_users(cls):
        return UserTable.query.all()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)

    def __repr__(self):
        return '<id {} : {} {}'.format(self.id, self.first_name, self.last_name)