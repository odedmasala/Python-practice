from pymongo import MongoClient
from bson import ObjectId

class StudentBL:
    def __init__(self):
        self.__mongo_client = MongoClient(port=27017)
        self.__db = self.__mongo_client["studentDB"]

    def get_all_students(self,name):
        students = []
        if name is None:
            pers_cursor = self.__db["students"].find()
        else:
            pers_cursor = self.__db["students"].find({ "FirstName" :  { "$regex" : name + '.*' }})
        for per in pers_cursor:
            students.append(per)
        
        return students

    def get_student(self,id):
        stud = self.__db["studnets"].find_one({ '_id' : ObjectId(id) })
        return stud

    def add_student(self,obj):
        per = {}
        per["FirstName"] = obj["FirstName"]
        per["LastName"] = obj["LastName"]
        per["Grades"] = obj["Grades"]
     

        self.__db["students"].insert_one(per)

        return "Created with ID : " + str(per["_id"])


    def update_student(self,id,obj):
        per = {}
        per["FirstName"] = obj["FirstName"]
        per["LastName"] = obj["LastName"]
        per["Grades"] = obj["Grades"]

        self.__db["students"].update_one({'_id' : ObjectId(id) } , {"$set" : per} )

        return "Udpated !"

    def delete_student(self,id):
        self.__db["students"].delete_one({'_id' : ObjectId(id) })

        return "Deleted !"



