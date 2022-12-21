from utils.db import db
from flask import Blueprint, jsonify, request

from models.Specie import Specie
from models.Pet import Pet
from models.Owner import Owner

pets = Blueprint('pet', __name__)

@pets.route('/api/pets')
def Read():
    try:
        arr = []
        requestedPets = Pet.query.all()
        for pet in requestedPets:
            pt = {
                "id": pet.id, 
                "name": pet.name,
                "age": pet.age, 
                "born_date": pet.born_date,
                "id_owner": pet.id_owner,
                "id_specie": pet.id_specie
            }
            arr.append(pt)
        return jsonify({"mensaje": arr}), 200

    except Exception as e:
        return jsonify({"mensaje": e.args})

@pets.route('/api/pets', methods=['POST'])
def Post():  
    try:
        name = request.json['name']
        age = request.json['age']
        born_date = request.json['born_date']
        id_owner = request.json['id_owner']
        id_specie = request.json['id_specie']

        owner = Owner.query.get(id_owner)
        specie = Specie.query.get(id_specie)

        if (owner is not None) and (specie is not None):
            pet = Pet(name = name, age = age, born_date = born_date, owner = owner, specie = specie)
            print(type(pet))
            db.session.add(pet)
            db.session.commit()
            return jsonify({"mensaje": "saved"}), 201

        return jsonify({"mensaje": "Not found related item"}), 404

    except Exception as e:
        return jsonify({"mensaje": e.args}), 500

