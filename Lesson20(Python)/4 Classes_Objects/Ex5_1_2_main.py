from Ex5_1 import Student
from Ex5_2 import School


s1 = Student(2)
s1.id = 1
s1.name=  "Ron"
s1.add_grade(100)
s1.add_grade(90)


s2 = Student(2)
s2.id = 2
s2.name=  "Gil"
s2.add_grade(80)
s2.add_grade(85)

school = School()
school.add_student(s1)
school.add_student(s2)

school.print_studnets_data()
    
      

        

    