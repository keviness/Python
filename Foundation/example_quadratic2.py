# quadratic4.py

import math
def main():
    print("Let us finds the solutions to a quadratic\n")
    a, b, c = eval(input("Do enter the coefficients (a, b, c):"))
    delta = b*b - 4*a*c
    if a == 0:
        x = -b / c
        print ("\nThere is an solution", x)
        
    

    else:
        disc = math.sqrt(delta)
        x1 = (-b + disc) / (2*a)
        x2 = (-b - disc) / (2*a)
        print("\nThe solutions are: ",x1, x2)

main()
