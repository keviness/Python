# try to draw 20181016.py

from turtle import *
def main():
    question = input("do you want to draw a triangle ?")
    setup(1000, 800, 0, 0)
    pensize(2)
    color("blue", 'pink')
    if question[0] in ['n', 'N']:
        draw(190, 90)
    else:
        print("It is wrong!")
        
def draw(width, angle):
    begin_fill()
    for i in range(4):
        fd(width)
        left(angle)
    end_fill()



main()
