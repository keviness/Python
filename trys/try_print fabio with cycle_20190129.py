#print Fabio with circle_20190129_py
n = eval(input("How many numbers:"))
f = []
def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        for i in range(n):
            f.append(fib(n-1)+fib(n-2))
            print(f)
 
if __name__ =="__main__":
    fib(n)
