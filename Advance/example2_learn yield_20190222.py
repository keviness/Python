#example2_learn yield_20190222
def fib(n):
    m, a, b = 0, 0, 1
    while m < n:
        yield b
        a, b = b, a+b
        m += 1
if __name__ == "__main__":
    f = fib(10)
    print("the fib is:", f.__next__())
    for i in f:
        print(i,)
