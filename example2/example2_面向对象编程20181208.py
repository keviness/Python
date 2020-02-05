# example2_面向对象编程20181208.py

class Student(object):

    def _init_(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s : %s" (self.name, self.score))

bart = Student("Bart Simpson", 50)
lisa = Student("Lisa Simpson", 98)
bart.print_score()
lisa.print_score()
