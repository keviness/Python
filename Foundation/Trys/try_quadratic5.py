# quadratic5.py

import math
def main():
    print("This program finds the real solutions to a quadratic\n")
    try:
        a, b, c = input("Please enter the cofficients(a, b, c):")
        discRoot = math.sqrt(b*b - 4*a*c)
        root1 = (-b + discRoot) / (2*a)
        root2 = (-b - discRoot) / (2*a)
        print("\nThe solutions are:",root1, root2)

    except ValueError:
        print("\nNo real roots")

main()
