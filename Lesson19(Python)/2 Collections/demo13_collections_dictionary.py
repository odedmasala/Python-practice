student = {"name": "Avi",
           "age": 30,
           "grades": [90, 88, 100],
           "address":
           {
               "city": "Eilat",
               "street":
               {
                   "name": "Herzel",
                   "no": 20
               }
           }
           }

print(student["address"]["street"]["name"])
print(student["grades"][1])
