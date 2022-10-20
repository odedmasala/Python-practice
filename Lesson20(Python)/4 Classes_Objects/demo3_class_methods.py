class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def print_data(self):
        print(f'Name: {self.name}, Age: {self.age}')

    def get_birth_year(self, current_year):
        return current_year - self.age

p = Person("Avi", 23)

p.print_data()

b_y = p.get_birth_year(2022)
print(b_y)