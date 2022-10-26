from flask import Blueprint, jsonify, request
from BLL.personsBLL import PersonsBLL




persons_bll = PersonsBLL()

persons = Blueprint("perosns", __name__)

# Get all persons
@persons.route("/", methods=["GET"])
def get_all_persons():
    persons = persons_bll.get_all_persons()
    return jsonify(persons)

@persons.route("/<string:id>", methods=["GET"])
def get_person(id):
    person = persons_bll.get_person(id)
    return jsonify(person)

@persons.route("/", methods=["POST"])
def add_person():
    pers = request.json
    status = persons_bll.add_person(pers)
    return jsonify(status)


@persons.route("/<string:id>", methods=["PUT"])
def update_person(id):
    pers = request.json
    status = persons_bll.update_person(id, pers)
    return jsonify(status)

@persons.route("/<string:id>", methods=["DELETE"])
def delete_person(id):
    status = persons_bll.delete_person(id)
    return jsonify(status)