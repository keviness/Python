#example_learn getattr and setattr_20190216
class Rectangle(object):

    def setsize(self, size):
        self.width, self.length = size
    def getsize(self):
        return self.width, self.length
    size = property(getsize, setsize)
if __name__ == "__main__":
    r = Rectangle()
    r.width, r.length = 3, 4
    print(r.width), print(r.length)
    print(r.size)
    print("*"*50)
    r.size = 30, 40
    print(r.width), print(r.length)
    print(r.size)
    
