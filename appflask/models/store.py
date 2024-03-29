from appflask.db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel')



    def __init__(self, name):
        self.name = name


    def __str__(self):
        return "User(id='%s')" % self.id


    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items]}


    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
