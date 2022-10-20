class Person: 
    def __init__(self):
        self.id = 0
        self.name = ''

class Employee(Person):
    def __init__(self):
        self.wid = 0
        self.department = ""
        

p = Person()
p.id = 1
p.name = "Ron"

e = Employee()
e.id = 2
e.name = "Gili"
e.wid = 0
e.department = "IT"

print(p.name)
print(p.id)
print(e.name)
print(e.id)