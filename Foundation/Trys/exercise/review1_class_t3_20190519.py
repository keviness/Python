#review_class_t3_20190519
class Students(object):
    def __init__(self, name, score, height):
        self.name = name
        self.score = score
        self.height = height
    def getheight(self):
        return self.height
    def printscore(self):
        print("{}\'s score is: {}".format(self.name, self.score))
    def introduct(self):
        print("Hello, {}!".format(self.name))
class College(Students):
    def verifysex(self):
        que = input("Are you a man?")
        if que in ["Y", "y"]:
            name_in = input("Enter your name:")
            self.introduct()
    def printscore(self):
        print("Hi, your score is : ", self.score)
    def printheight(self):
        print("Your height is:", self.height)
if  __name__ == "__main__":
    Nancy = College("nancy", 98, 190)
    Nancy.printheight()
    Nancy.printscore()
    Nancy.verifysex()
