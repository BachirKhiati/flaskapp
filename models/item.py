from db import db

class ItemModel(db.Model):

    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    picture_uri= db.Column(db.String(300))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')



    def __init__(self, name, price, picture_uri,store_id):
        self.name = name
        self.price = price
        self.picture_uri = picture_uri
        self.store_id = store_id

    def __str__(self):
        return "User(id='%s')" % self.id


    def json(self):
        return {'name': self.name, 'price': self.price, 'picture_uri':  self.picture_uri}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
