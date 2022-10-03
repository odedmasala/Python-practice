arr = [{"id" : 1, "name" : "Ron"},
        {"id" : 2, "name" : "Dana"},
        {"id" : 3, "name" : "Avi"}]


# Get ONLY the items with name that starts with "D"

arr2 = list(filter(lambda user: user["name"].startswith("D"), arr))
print(arr2)