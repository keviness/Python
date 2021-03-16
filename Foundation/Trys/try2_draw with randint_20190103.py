#try to draw a circle with for, random_20190103.py

from turtle import *
from random import *

def main():
    setup(1200, 1000, 0, 0)
    pensize(2)
    color("red", 'pink')
    for i in range(5):
        rad = randint(80, 200)
        angle = randint(200, 360)
        drawcircle(rad, angle)

def drawcircle(rad, angle):
    begin_fill()
    circle(rad, angle)
    end_fill()
main()
