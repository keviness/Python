import turtle

def main():
    
    turtle.setup(1300, 800, 0, 0)
    turtle.pensize(10)
    turtle.color('pink')
    turtle.seth(0)
    drawCircle(150, 360)


def drawCircle(rad, angle):

    for i in range(5):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
main()
