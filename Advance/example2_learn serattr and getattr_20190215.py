#example_learn setattr and getattr_2019.2.15
class NewRectangle(object):
    def __init__(self):
        self.width = 0
        self.length = 0
    def __setattr__(self,name,value):
        if name == "size":
            self.width, self.length = value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        if name == "size":
            return self.width, self.length
        else:
            raise AttributeError
if __name__ == "__main__":
    r = NewRectangle()
    r.width, r.length = 3, 4
    print(r.size)
    r.size = 30, 40
    print(r.width), print(r.length)
    
        
