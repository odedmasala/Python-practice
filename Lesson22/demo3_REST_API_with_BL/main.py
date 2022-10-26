from flask import Flask
from flask import jsonify
from flask import request

from BL.cars import *

car_bl = CarBL()

app = Flask(__name__)

@app.route("/cars", methods=["GET"])
def get_all_cars():
    cars = car_bl.get_all_cars()
    return jsonify(cars)


@app.route('/cars/<string:id>',methods=['GET'])
def get_car(id):
    car = car_bl.get_car(id)
    return jsonify(car)

@app.route('/cars',methods=['POST'])
def create_car():
    car_bl.add_car(request.json)
    return jsonify(car_bl.get_all_cars())

@app.route('/cars/<string:id>', methods=['PUT'])
def update_car(id):
    car_bl.update_car(id, request.json)
    return jsonify(car_bl.get_all_cars())

@app.route('/cars/<string:id>', methods=['DELETE'])
def delete_car(id):
    car_bl.delete_car(id)
    return jsonify(car_bl.get_all_cars())

app.run()