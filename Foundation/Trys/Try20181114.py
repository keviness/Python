# Try draw circle 2018.11.14

from turtle import *

def main():
    setup(1000, 800, 0, 0)
    color("red", 'blue')
    pensize(8)
    draw(100, 120)


def draw(rad, angle):
    begin_fill()
    for i in range(10):
        circle(rad, angle)
        fd(rad * 2)
        left(angle)
    end_fill()

main()

    
    
