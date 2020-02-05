#review1_class_t1_20190511
class Person(object):
    def __init__(self, name, lang="language", website="www.keviness.com"):
        self.name = name
        self.lang = lang
        self.website = website
    def get_name(self, name):
        print("The name is %s" % self.name)
kevin = Person("bob")
Bob = Person("china")
print("kevin:",kevin.name)
Bob.get_name("Lucy") 
print("Candy:",Bob.name)
