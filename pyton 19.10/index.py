import json
import os
import sys
import requests
# path = os.path.join(sys.path())



def get_user(user_id):
    url = 'https://jsonplaceholder.typicode.com/users'
    resq = requests.get(url)
    data = resq.json()
    user = list(filter(lambda us: us["id"] == user_id, data))
    return user

print(get_user(1))