# try-draw a triangle-20181206.py
from turtle import *
def drawtriangle(rad, angle):
    begin_fill()
    for i in range(3):
        fd(rad)
        left(angle)
    end_fill()

def drawcircle(wid, angle1):
    begin_fill()
    circle(wid, angle1)
    end_fill()

def main():
    Q = input("what do you want to draw(circle or triangle):")    
    setup(1000, 900, 0, 0)
    pensize(10)
    color("blue", 'red') 
    if Q[0] in ["C", 'c']:
        drawcircle(79, 360)
    elif Q[0] in ["T", 't']:
        drawtriangle(90, 120)
    else:
        print("sorry, it is wrong")

main()
