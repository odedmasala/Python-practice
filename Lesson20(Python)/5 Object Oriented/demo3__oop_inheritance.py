class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def print_data(self):
        print(self.name)
        print(self.id)


class Employee(Person):
    def __init__(self, id, name,dep):
        super().__init__(id, name)
        self.department = dep
    def print_data(self):
        super().print_data()
        print(self.department)


e = Employee(0, "Avi", "CS")
e.print_data()
p = Person(1, "Moshe")
p.print_data()
