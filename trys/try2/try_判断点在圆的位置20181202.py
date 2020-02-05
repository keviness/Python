#try 判断点是否在圆外—20181202.py
from math import sqrt 
def cal(a, b, r, x, y):
    d = sqrt((x - a)**2+(y - b)**2)
    if d < r:
        print("the point is in the circle")
    elif d == r:
        print("the point is on the circle")
    else:
        print("the point is uot the circle")

def main():
    a, b, r = eval(input("what \'s the circle?(a, b, r)"))
    x, y = eval(input("What\'s the point ?(x, y)"))
    cal(a, b, r, x, y)
main()
