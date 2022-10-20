class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Dana")
print(p1.name)
print(p1.age)