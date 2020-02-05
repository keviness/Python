#example2_learn setattr and getattr_20190216
class A(object):
    def __getattr__(self, name):
        print("Using getattr")
        
    def __setattr__(self, name, value):
        print("Using setattr")
        self.__dict__[name] = value
        return self.value

    
        
