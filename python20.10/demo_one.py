import requests
# from pymongo import MongoClient
# from bson import ObjectId

url = "https://api.tvmaze.com/shows"

# Get All
resp = requests.get(url)
data = resp.json()
