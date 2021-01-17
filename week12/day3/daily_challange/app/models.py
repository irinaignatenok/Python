
from . import db

class User(db.Model):

    id = db.Column(db.Integer(), primary_key = True, autoincrement = True)
    name = db.Column(db.String(64), nullable = False, unique = True)
    age = db.Column(db.Integer())
