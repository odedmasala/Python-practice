import requests
from pymongo import MongoClient


# resp = requests.get("https://api.tvmaze.com/shows")
# shows = resp.json()
# shows = shows[0:10]

# shows = list(map(lambda show: {
# "name": show["name"], 
# "genres": show["genres"],
# "rating": show["rating"]["average"]
# }, shows))

client = MongoClient("localhost", 27017)
db = client["moviesDB"]
movies_col = db["movies"]

# movies_col.insert_many(shows)

current_name = input("Enter show name:")
new_name = input("Enter new show name:")

obj = {"name": new_name}
movies_col.update_one({"name": current_name}, {"$set": obj})