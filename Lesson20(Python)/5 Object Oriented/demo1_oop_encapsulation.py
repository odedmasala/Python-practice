class Person:
    def __init__(self):
        self.name = ""
        self.__phones = []
    def add_phone(self, phone):
        if len(phone) == 7:
            self.__phones.append(phone)
        else: 
            print("The phone is invalid")
    def print_phones(self):
        print(self.__phones)
        # self.__func1()
    def __func1(self):
        print("hello from func1")
        

p = Person()
p.name = "Ron"
p.add_phone("052-222")
p.__func1()
# p.__phones.append("1234567")
p.print_phones()