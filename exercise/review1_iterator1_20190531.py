#review1_iterator1_20190531
'''built a private iterator'''

class MyIterator(object):
    def __init__(self, n):
        self.o = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > self.o:
            o = self.o
            self.o += 1
            return o
        else:
            raise StopIteration
if __name__ == "__main__":
    pri = MyIterator(10)
    for i in pri:
        print(i)
    
