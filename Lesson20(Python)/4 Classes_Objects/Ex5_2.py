class School:
    def __init__(self):
        self.studnets = []

    def add_student(self,s):
        arr = list(filter( lambda x : x.id == s.id ,self.studnets))
        if len(arr) == 0:
            self.studnets.append(s)
        else:
            print("Student already registered")

    def print_studnets_data(self):
        for s in self.studnets:
            s.print_data()

        

    
      

        

    