#example2_迭代器2_20190222
class Fibs(object):
    def __init__(self, Max):
        self.Max = Max
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        fib = self.a
        if fib > self.Max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
if __name__ == "__main__":
    fibs = Fibs(5)
    print(list(fibs))
