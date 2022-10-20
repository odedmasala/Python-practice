from copyreg import constructor


class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

p1 = Person()
p1.name = "Ron"
p1.age = 30

p2 = Person()
p2.name = "Michael"
p2.age = 25

# PAY ATTENTION - THIS IS AN ARRAY OF PERSON OBJECTS
li = [p1,p2]
print(type(p1))
print(type(5))



for per in li:
    print(per.name)