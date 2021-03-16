#print Fabio_2019.01.29_py

def fabio():
    n = eval(input("How many numbers:"))
    lst = [1,1]
    for i in range(n):
        lst.append(lst[-1]+lst[-2])
    print(lst)
fabio()
    
