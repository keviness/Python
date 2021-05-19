# quadratic.py


import math

def main():
    print("This program finds the real solutions to a quadratic\n")
    a, b, c= eval(input("Please enter the coefficients(a, b, c):"))
    delta = b*b - 4*a*c
    if delta < 0:
        print ("\nThe equantion has no real roots!")
    else:
        delta = math.sqrt(delta)
        root1 = (-b + delta) / (2*a)
        root2 = (-b - delta) / (2*a)
        print("\nThe solution are:", root1, root2)


main()
    
