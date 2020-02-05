#example2_learn class object2_20190224
class Person(object):
    def __init__(self, name, lang="golang", website="www.com"):
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "qiwsir"
if __name__ == "__main__":
    key = Person("kevin")
    info = Person("lucy", lang="Python", website="hello world!")
    print(key.name)
    print(key.email)
    print(info.lang)
    print(info.website)
    print(info.email)
        
    
