# try_2018-11-18

from turtle import  *

def main():
    q = input("do you want draw?")
    if q[0] in ['Y', 'y']:
        
        setup(1000, 900, 0, 0)
        color('red', 'blue')
        pensize(3)
        draw(100, 145)
    else:
        print("sorry")


def draw(rad, angle):
    begin_fill()
    for i in range(5):
        fd(rad)
        left(angle)
    end_fill()
    
main()
