# exercise2 fibonacci.py

def main():
    
    n = eval(input("how many fibonacci do you want to print:"))
    x = 1
    y = 1
    print (x),print (y)
    
    i = 2
    while i < n:
        z = x + y
        print (z)
        x = y
        y = z
        i += 1

        
main()
