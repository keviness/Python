#example_learn getatter,setatter_2019.2.15
class A(object):
    author = "kevin"
    def __getattr__(self,name):
        if name != "author":
            return "from starter to master"
if __name__ == "__main__":
    a = A()
    print(a.author)
    print(a.lang)
        
