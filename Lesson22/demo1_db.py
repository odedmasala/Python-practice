from pymongo import MongoClient
from bson import ObjectId

# Connecting to MongoDB
client = MongoClient("localhost", 27017)

db = client["personsDB"]
collection = db["persons"]


# READ ALL
# persons = collection.find()
# print(list(persons))
# for person in persons:
#     print(person)
#     print(person["name"])

# get document by its id
# person = collection.find_one({"_id": ObjectId("6350f42a6228e154cf704587") })
# print(person["name"])
# print(person)


# Create a new document
# doc = {"name": "Yael", "age": 27}
# collection.insert_one(doc)
# collection.insert_many(doc,doc)


# doc = {"name": "Gil"}
# collection.update_one({"_id": ObjectId("6350f59a43c7128eca81e68b")}, {"$set": doc})

# doc = {"city": "Lod"}

# collection.update_many({"city": "Afula"}, {"$set": doc})


# collection.delete_one({"_id": ObjectId("6350f59a43c7128eca81e68b")})
# collection.delete_many({"city": "Lod"})

