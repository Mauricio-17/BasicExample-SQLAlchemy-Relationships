from utils.db import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    born_date = db.Column(db.DateTime)
    id_owner = db.Column(db.String(8), db.ForeignKey('owner.dni'))
    id_specie = db.Column(db.String(5), db.ForeignKey('specie.id'))
