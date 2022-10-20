import requests

new_car = {}
id = int(input("Enter car id"))
model = input("Enter car model")

new_car["id"] = id
new_car["model"] = model

resp = requests.post("http://127.0.0.1:5000/cars", json=new_car)
