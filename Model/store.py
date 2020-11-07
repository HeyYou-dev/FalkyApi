import sqlite3
from db import db


class StoreModel(db.Model):


    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f"StoreModel({self.name})"


    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}


    @classmethod
    def get_by_name(cls, name):
        """connecton = sqlite3.connect('data.db')

        cursor = connecton.cursor()

        query = "SELECT * from items where Name =?"

        result = cursor.execute(query, (name,))

        row = result.fetchone()

        if row:

            return cls(*row)"""
        a=cls.query.filter_by(name=name).first()
        print(a)
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
