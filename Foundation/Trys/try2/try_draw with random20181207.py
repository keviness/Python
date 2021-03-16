# try-random库应用于turtle-20181207.py
from random import randint
from turtle import *
def draw(rad, angle):
    begin_fill()
    for i in range(5):
        fd(rad)
        left(angle)
    end_fill()

def drawcircle(wid, angle1):
    begin_fill()
    circle(wid, angle1)
    end_fill()
    
def main():
    Q = input("what do you want to draw?")
    setup(1000, 900, 0, 0)
    pensize(2)
    color("blue", 'red')
    if Q[0] in ["T", 't']:  
        a, b = randint(200, 300), randint(135, 250)
        draw(a, b)
    elif Q[0] in ["C", 'c']:
        wid, angle1 = randint(170, 200), randint(280, 360)
        drawcircle(wid, angle1)
    else:
        print("The wrong")
main()
