import json
from bson import ObjectId
from flask import Flask
from flask import jsonify
from flask import request

from BL.studentBL import *

app = Flask(__name__)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj)

app.json_encoder = MyEncoder


stud_bl = StudentBL()

@app.route('/students', methods=['GET'])
def get_all_students():
    name = request.args.get('name')
   
    studs = stud_bl.get_all_students(name)
    return jsonify(studs)

@app.route('/students/<string:id>', methods=['GET'])
def get_student(id):
    stud = stud_bl.get_student(id)
    return jsonify(stud)

@app.route('/students', methods=['POST'])
def add_student():
    status = stud_bl.add_student(request.json)
    return jsonify(status)

@app.route('/students/<string:id>', methods=['PUT'])
def update_student(id):
    status = stud_bl.update_student(id, request.json)
    return jsonify(status)

@app.route('/students/<string:id>', methods=['DELETE'])
def delete_student(id):
    status = stud_bl.delete_student(id)
    return jsonify(status)

app.run()

