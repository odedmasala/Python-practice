class Student:
    def __init__(self,max_grades):
        self.id = 0
        self.name = ""
        self.grades = []
        self.max_grades = max_grades

    def print_data(self):
        print(self.id)
        print(self.name)
        print(self.grades)

    def add_grade(self, grade):
        if len(self.grades) < self.max_grades:
            self.grades.append(grade)
        else:
            print("No more space for new grades")

    def get_avg(self):
        return sum(self.grades) / len(self.grades)


        

    