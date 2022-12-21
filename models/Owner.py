from utils.db import db

class Owner(db.Model):
    dni = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20))
    cellphone = db.Column(db.String(9))
    pets = db.relationship('Pet', backref='owner')


