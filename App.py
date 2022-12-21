from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.owner import owners
from routes.specie import species
from routes.pet import pets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1q2w3e4r5t@localhost/vetSys'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

SQLAlchemy(app)

# ROUTES
app.register_blueprint(owners)
app.register_blueprint(species)
app.register_blueprint(pets)
