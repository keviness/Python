#review1_class_t5_20190524
class ProtectMe(object):
    def __init__(self):
        self.me = "Crisis"
        self.__name = "privilige"
    def getname(self):
        print("hello", self.__name)
    def __getname(self):
        print("It\'s a private method")

    def visitprimethod(self):
        print(self.__name)
        self.__getname()
        
    @property
    def printname(self):
        print(self.__name)
        self.__getname()

