class Animal:
    def __init__(self, nol):
        self.num_of_legs = nol

    def eat(self):
        print("Animal is eating")


class Zebra(Animal):
    def __init__(self, nol, nos):
        super().__init__(nol)
        self.num_of_strips = nos

    def print_data(self):
        print(self.num_of_legs)
        print(self.num_of_strips)

    # Polymorphism - Method Overriding
    def eat(self):
        print("Zebra is eating")


class Monkey(Animal):
    def __init__(self, nol, color):
        super().__init__(nol)
        self.color = color

    def print_data(self):
        print(self.num_of_legs)
        print(self.color)

    # Polymorphism - Method Overriding
    def eat(self):
        print("Monkey is eating")


class Chimpanzee(Monkey):
    def __init__(self, nol, color, height):
        super().__init__(nol, color)
        self.height = height

    def print_data(self):
        super().print_data()
        print(self.height)


class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def count_animals(self):
        print(len(self.__animals))

    def feed(self):
        for a in self.__animals:
            a.eat()


a = Animal(4)
z = Zebra(4, 100)
m = Monkey(2, "Brown")
c = Chimpanzee(2, "Black", 170)

zoo = Zoo()
zoo.add_animal(a)
zoo.add_animal(z)
zoo.add_animal(m)
zoo.add_animal(c)

zoo.count_animals()

zoo.feed()
