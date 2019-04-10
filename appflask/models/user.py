from sqlalchemy import text as sa_text
from sqlalchemy.dialects.postgresql import UUID

from appflask import bcrypt
from appflask.db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    date_of_birth = db.Column(db.String(80))
    profile_picture_uri = db.Column(db.String(80))

    # def __init__(self, username, password, email, first_name, last_name, gender, date_of_birth, profile_picture_uri):
    def __init__(self, username, email, password, first_name, last_name):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        # self.gender = gender
        # self.date_of_birth = date_of_birth
        # self.profile_picture_uri = profile_picture_uri

    def __str__(self):
        return "User(id='%s')" % self.id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        query = cls.query.filter_by(email=email).first()
        print('query')
        print(query)
        return query

    @classmethod
    def find_by_uuid(cls, _uuid):
        return cls.query.filter_by(id=_uuid).first()

    @classmethod
    def check_password_database(self, password_hash, password):
        print('pass')
        print('pass')
        print('pass')
        print('pass')
        print(password)
        print(self.password)
        print(UserModel.password)
        print('pass')

        token = bcrypt.check_password_hash(password_hash, password)
        print('token')
        print('token')
        print('token')
        print('token')
        print(token)
        print('token')
        return token
