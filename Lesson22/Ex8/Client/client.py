import requests 


obj = {}
id = int(input("Enter car id"))
model = input("Enter car model")
year = input("Enter car model")


obj["id"] = id
obj["model"] = model
obj["year"] = year
obj["colors"] = ["Black", "White"]
obj["driver"] = {}
obj["driver"]["FirstName"] = "Dana"
obj["driver"]["LastName"] = "Levy"

resp = requests.post("http://127.0.0.1:5000/cars", json=obj)
resp1 = requests.get("http://127.0.0.1:5000/cars")
cars = resp1.json
print(cars)