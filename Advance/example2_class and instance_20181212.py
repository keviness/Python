# example2 - class and instance-20181212.py

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print("%s : %s" %(self.name, self.score))
    def get_grade(self):
        if self.score >= 80:
            return "A" 
        elif self.score >=60:
            return "B"
        else:
            return "C" 
bart = Student("Bart", 59)
lisa = Student("Lisa", 89)
   
