import requests

url = "https://jsonplaceholder.typicode.com/users"

# # Get All
# resp = requests.get(url)
# data = resp.json()

# for user in data:
#     print(user["name"])


# # Get By ID
# resp = requests.get(f"{url}/2")
# data = resp.json()
# print(data["name"])


# # Add a new user
# obj = {"name": "Avi", "age": 30}
# resp = requests.post(url, obj)
# data = resp.json()
# print(data)


# # Update a user
# obj = {"name": "Dana", "age": 40}
# resp = requests.put(f"{url}/7", obj)
# data = resp.json()
# print(data)


# Delete a user
resp = requests.delete(f"{url}/5")
data = resp.json()
print(data)
