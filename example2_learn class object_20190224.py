#example2_ learn class object_20190224
class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def color(self, color):
        print("%s is %s"%(self.name, color))
        
    
