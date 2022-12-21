from utils.db import db

class Specie(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(30))
    pets = db.relationship('Pet', backref='specie')