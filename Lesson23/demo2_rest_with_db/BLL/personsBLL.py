from pymongo import MongoClient
from bson import ObjectId

class PersonsBLL:
    def __init__(self):
        self.__client = MongoClient(port=27017) # CONNECT TO MONGO DB
        self.__db = self.__client["personsDB"] # CONNECT TO DB
        self.__collection = self.__db["persons"] # CONNECT TO COLLECTION
    def get_all_persons(self):
        persons = list(self.__collection.find({}))
        return persons

    def get_person(self, id):
        person = self.__collection.find_one({"_id": ObjectId(id)})
        return person

    def add_person(self, obj):
        self.__collection.insert_one(obj)
        return "Created"

    def update_person(self,id, obj):
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": obj})
        return "Updated!"

    def delete_person(self,id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return "Deleted!"

