import sqlite3
from db import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    date_of_birth = db.Column(db.String(80))
    profile_picture_uri = db.Column(db.String(80))

    # def __init__(self, username, password, email, first_name, last_name, gender, date_of_birth, profile_picture_uri):
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        # self.first_name = first_name
        # self.last_name = last_name
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
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        print('id')
        print('id')
        print('id')
        print(_id)
        print(str(_id))
        return cls.query.filter_by(id=str(_id)).first()