#example2_learn Encapsulation_20190218
class ProtectMe(object):
    def __init__(self):
        self.me = "python"
        self.__namey = "kevin"
    @property
    def name(self):
        print("hey")
        return self.__namey
 
if __name__ == "__main__":
    p = ProtectMe()
    print(p.name)
