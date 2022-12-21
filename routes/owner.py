from utils.db import db
from flask import Blueprint, jsonify, request

from models.Owner import Owner
from models.Pet import Pet

owners = Blueprint('owner', __name__)


@owners.route("/api/owners")
def Read():
    try:
        arr = []
        arrOwners = Owner.query.all()
        for owner in arrOwners:
            ow = {"dni": owner.dni, "name": owner.name,
                  "lastname": owner.lastname,
                  "cellphone": owner.cellphone}
            arr.append(ow)

        return jsonify({"mensaje": arr}), 200

    except Exception as e:
        return jsonify({"mensaje": e.args}), 500

@owners.route('/api/owners', methods=['GET', 'POST'])
def Create():
    try:
        dni = request.json['dni']
        name = request.json['name']
        lastname = request.json['lastname']
        cellphone = request.json['cellphone']
        
        owner = Owner(dni=dni, name=name, lastname=lastname, cellphone=cellphone)
        print(dni)
        db.session.add(owner)
        db.session.commit()
        return jsonify({"mensaje": "saved"}), 201

    except Exception as e:
        return jsonify({"mensaje": e.args}), 500

@owners.route('/api/owners/<dni>', methods=['PUT'])
def Update(dni):
    try:
        owner = Owner.query.get(dni)
        if owner is not None:
            owner.name = request.json['name']
            owner.lastname = request.json['lastname']
            owner.cellphone = request.json['cellphone']
            db.session.commit()

            return jsonify({"mensaje": "Updated Item"}), 200
        return jsonify({"mensaje": "Item not found"}), 404
    except Exception as e:
        return jsonify({"mensaje": e.args}), 500

@owners.route('/api/owners/<dni>', methods=['DELETE'])
def DeleteItem(dni):
    try:
        owner = Owner.query.get(dni)
        if owner is not None:
            db.session.delete(owner)
            db.session.commit()
            return jsonify({"mensaje": "Deleted Item"}), 200

        return jsonify({"mensaje": "Item not foubd"}), 404
    except Exception as e:
        return jsonify({"mensaje": e.args}), 500
