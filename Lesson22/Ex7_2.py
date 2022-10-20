import requests
import json
import os
import sys

user_id = input("Enter id")

resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
user = resp.json()

print(user["name"])
print(user["email"])

if user["name"].startswith("E"):
   resp =  requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
   user_todos = resp.json()
   titles = list(map(lambda todo: todo["title"], user_todos))

obj = {"titles": titles}

path = os.path.join(sys.path[0], 'user_todos.json')


with open(path, 'w') as f:
    json.dump(obj, f)


