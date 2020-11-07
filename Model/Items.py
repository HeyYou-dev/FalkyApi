import sqlite3
from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.String(80))
    store_id =db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price,store_id):
        self.name = name

        self.price = price

        self.store_id= store_id


    def __repr__(self):

        return f"ItemModel({self.name},{self.price})"


    def json(self):

        return {'name': self.name, 'price': self.price,'store_id':self.store_id}


    @classmethod
    def get_by_name(cls, name):

        """connecton = sqlite3.connect('data.db')

        cursor = connecton.cursor()

        query = "SELECT * from items where Name =?"

        result = cursor.execute(query, (name,))

        row = result.fetchone()

        if row:

            return cls(*row)"""

        return cls.query.filter_by(name=name).first()

    def save_to_db(self):

        """connecton = sqlite3.connect('data.db')

        cursor = connecton.cursor()

        query = "INSERT into items  values (?,?) "

        cursor.execute(query, (self.name, self.price))

        connecton.commit()

        connecton.close() """

        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
