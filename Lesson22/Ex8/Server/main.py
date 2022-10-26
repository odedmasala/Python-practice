from flask import Flask
from flask import jsonify
from flask import request



# Create web app
app = Flask(__name__)


# Create fake data source
cars = [{"id" : 1, "model" : "Mazda", "year" : 2019, "colors" : ["Red","White"],
         "driver" : {"FirstName" : "Avi", "LastName" : "Cohen"} }]

@app.route('/cars', methods=["GET"])
def get_all_cars():
    return jsonify(cars)


@app.route('/cars/<string:id>', methods=["GET"])
def get_car(id):
    arr = list(filter(lambda car: car["id"] == int(id), cars))
    return jsonify(arr[0])

@app.route('/cars', methods=["POST"])
def create_car():
    data = request.json
    cars.append(data)
    return jsonify(cars)


@app.route('/cars/<string:id>', methods=["PUT"])
def update_car(id):
    data = request.json
    for car in cars:
        if car["id"] == int(id):
            car["model"] = data["model"]
            car["colors"] = data["colors"]
            car["year"] = data["year"]
            car["driver"] = data["driver"]
            break
    return jsonify(cars)


@app.route("/cars/<string:id>", methods=["DELETE"])
def delete_car(id):
    index = -1
    for i in range(len(cars)):
        if cars[i]["id"] == int(id):
            index = i
            break
    cars.pop(index)
    return jsonify(cars)

app.run()