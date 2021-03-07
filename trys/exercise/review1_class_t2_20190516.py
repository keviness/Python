#review_class_t2_20190516
class Person(object):
    color = "white"
    def eyes(self):
        print("two eyes")
    def skincolor(self, color):
        print("The skincolor is:", color)
class Girl(object):
    age = 20
    def height(self, h):
        print("The height is:",h )
class HotGirl(Person, Girl):
    def __init__(self,  name):
        self.name = name
    def instroduce(self, color, m):
        print("{} is a hotgirl, her skincolor is:{} \nher height is{}".format(self.name, color, m))
if __name__ == "__main__":
    Lucy = HotGirl("lucy")
    Lucy.instroduce("black", 190)
    Lucy.height(170)
    Lucy.skincolor("Pink")
    print("{} is a hotgirl, she is {}".format(Lucy.name, Lucy.age))
    
        
