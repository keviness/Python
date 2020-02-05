# try turtle2.20181014.py

from turtle import *

def main():
    setup(1000, 800, 0, 0)
    color("blue", 'red')
    pensize(3)
    draw(200, 144)
    

def draw(rad, angle):
    begin_fill()
    for i in range(5):
        forward(rad)
        left(angle)
    end_fill()
main()
