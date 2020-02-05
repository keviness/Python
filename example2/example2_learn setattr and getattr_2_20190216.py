#example2_learn setattr and getattr_20190216
class B(object):
    def __getattribute__(self, name):
        print("Using getattribute")
        return object.__getattribute__(self,name)
