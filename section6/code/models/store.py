# Import SQL Alchemy for database management
from db import db

# Initialise the store model and inherit the db class
class StoreModel(db.Model):

    ## Define the database table name
    __tablename__ = 'stores'

    ## define the columns of  stores tables
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    ## Initialise the class
    def __init__(self, name):
        self.name = name

    ## Return the json format of a store object
    def json(self):
        return {'name':self.name, 'items':[item.json() for item in self.items.all()]}

    ## find a store by name
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    ### Save to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    ## Delete from store table
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
