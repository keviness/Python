# two point distance.py

import math

def square (x):
    return x * x
def distance (x1, x2, y1, y2):
    dist = math.sqrt(square(x1 - x2) + square(y1 - y2))
    return dist
def istriangle (x1, y1, x2, y2, x3, y3):
    flag = ((x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)) != 0
    return flag
def main ():
    print("Please enter (x,y) of three points in turn:")
    x1,y1 = eval(input("point1:"))
    x2,y2 = eval(input("point2:"))
    x3,y3 = eval(input("point3:"))
    if(istriangle(x1, y1, x2, y2, x3, y3)):
        perim = distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + distance(x1, y1, x3, y3)
        print("The perimeter of the triangle is :{0:.2f}".format(perim))

    else:
        print("kidding me ? it is not a triangle.")

main()
        
