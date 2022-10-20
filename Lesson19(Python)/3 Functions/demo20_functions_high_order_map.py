arr = [{"id" : 1, "name" : "Ron"},
        {"id" : 2, "name" : "Dana"},
        {"id" : 3, "name" : "Avi"}]


arr2 = list(map(lambda user: user["name"], arr))
print(arr)
print(arr2)