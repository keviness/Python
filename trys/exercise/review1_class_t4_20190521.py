#review1_class_t4_20190521
class StaticMethod(object):
    @staticmethod
    def foo():
        print("This is a staticmethod:foo()")
class ClassMethod(object):
    @classmethod
    def bar(cls):
        print("this is a classmethod:bar()")
        print("it is a classmethod:", cls.__name__)
if __name__ == "__main__":
    static_foo = StaticMethod()
    static_foo.foo()
    StaticMethod.foo()
    print("*"*30)
    class_bar = ClassMethod()
    class_bar.bar()
    ClassMethod.bar()
