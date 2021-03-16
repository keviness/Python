# try to draw20181019.py

from turtle import *
def main():
    ques = input("we will draw:")
    title = "Many circle"
    setup(1000, 800, 0, 0)
    pensize(3)
    speed(5)
    
    if ques[0] in ['Y', 'y']:
        seth(60)
        color("red", 'green')
        draw(100, 360)
    else:
        color("pink", 'red')
        drawtriangle(120, 60)
        

def draw(rand, angle):
    begin_fill()
    for i in range(5):
        fd(rand)
        circle(rand, angle)
    end_fill()

def drawtriangle(rad, angle1):
    begin_fill()
    for i in range (3):
        fd(rad)
        left(angle1)
    end_fill()
    
main()

    
