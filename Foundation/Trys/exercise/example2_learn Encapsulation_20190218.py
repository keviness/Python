#example2_learn Encapsulation_20190218
class ProtectMe(object):
    def __init__(self):
        self.me = "qiwer"
        self.___me = "Lucy"
    def __print(self):
        print("hello python world!")
    def code(self):
        print("What do you want to represent ?")
        self.__print()
if __name__ == "__main__":
    t = ProtectMe()
    print(t.me)
    t.code()
    
