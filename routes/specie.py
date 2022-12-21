from utils.db import db
from flask import Blueprint, jsonify, request
import json
from models.Specie import Specie
from models.Pet import Pet

species = Blueprint('specie', __name__)

@species.route("/api/species")
def Read():
    try:
        arr = []
        arrEspecies = Specie.query.all()
        for especie in arrEspecies:
            sp = {"id": especie.id, "name": especie.name, "description": especie.description}
            arr.append(sp)            
        
        return jsonify({"mensaje": arr})

    except Exception as e:
        return jsonify({"mensaje": e.args})

@species.route('/api/species', methods=['POST'])
def Create():  
    try:
        id = request.json['id']
        name = request.json['name']
        description = request.json['description']
        
        specie = Specie(id = id, name = name, description = description)
        print(id)
        db.session.add(specie)
        db.session.commit()
        return jsonify({"mensaje": "saved"}), 201
    except Exception as e:
        return jsonify({"mensaje": e.args}), 500


@species.route('/api/species/<id>', methods=['PUT'])
def UpdateItem(id):
    try:
        specie = Specie.query.get(id)
        if specie is not None:
            specie.name = request.json['name']
            specie.description = request.json['description']
            db.session.commit()

            return jsonify({"message": "updated item"})
        return jsonify({"message": "item not found"}), 404
    except Exception as e:
        return jsonify({"mensaje": e.args}), 500

@species.route('/api/species/<id>', methods=['DELETE'])
def DeleteItem(id):
    try:
        specie = Specie.query.get(id)
        if specie is not None:
            db.session.delete(specie)
            db.session.commit()
            return jsonify({"message": "deleted item"})
        return jsonify({"message": "item not found"}), 404
    except Exception as e:
        return jsonify({"mensaje": e.args}), 500


