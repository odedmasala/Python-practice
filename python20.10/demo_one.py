from concurrent.futures import process
import requests
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()
# os.environ
# client = MongoClient(process.env)
# url = "https://api.tvmaze.com/shows"
DB_URL = os.environ.get("DB_URL") 
print(DB_URL)
# Get All
# resp = requests.get(url)
# data = list(resp.json())[0:9]
# store_data = list(map(lambda movie:{"name":movie["name"],"genres":movie["genres"],"rating":movie["rating"]["average"]},data))
# db = client["movieClass"]
# collection = db["movie"]

# # print(list(hotels))
# collection.insert_many(store_data)
# print(store_data)
