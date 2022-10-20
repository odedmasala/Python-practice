# Magic or Dunder Methods

class Person:
    def __init__(self, age=18):
        self.name = "Avi"
        self.age = age
    def __gt__(self,other):
        return self.age > other.age
    def __str__(self):
        return f'Name {self.name} Age {self.age}' # will only executes when printing the object
        # in js 'name: ${}' # js
    def __add__(self,other):
       return self.age + other
        

p1 = Person()
p2 = Person()

p3 = p1 + 2
print(p3)


# if p1 > p2:
#     print(p1.name, "Cohen")
# else: 
#     print(p2.name, "Levy")