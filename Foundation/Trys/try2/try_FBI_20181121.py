# try FBI 20181121.py

def main():
    n = eval(input("how many:"))
    a, b , i= 1, 1, 0
    while i < n:
        s = a + b
        a, b = b, a+b
        i = i +1
        print(s)
main()
