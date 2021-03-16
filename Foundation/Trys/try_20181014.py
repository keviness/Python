# try turtle2018.10.14.py
import turtle

def main():
    turtle.setup(1000, 800, 0, 0)
    turtle.speed(4)
    turtle.pensize(2)
    turtle.color("green", 'red')   
    draw(80, 360)
    
def draw(rad, angle):
    turtle.begin_fill()
    for i in range(9):
        turtle.circle(rad, angle)
        turtle.fd(rad/2)
        turtle.right(rad)
        turtle.goto(0, 3)
    turtle.end_fill()
    
main()
