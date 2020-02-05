import turtle

def main():

    turtle.setup(1300, 800, 0, 0)
    turtle.pensize(3)
    turtle.color('blue')
    turtle.seth(0)

    draw(100, 90)


def draw(rad, angle):

    turtle.seth(0)
    turtle.fd(rad)
    turtle.seth(angle)
    turtle.fd(rad)
    turtle.seth(-180)
    turtle.fd(rad)
    turtle.seth(-angle)
    turtle.fd(rad)

    for i in range(4):
        turtle.color('green')
        turtle.seth(180)        
        turtle.fd(rad)
        turtle.color('pink')
        turtle.seth(angle)
        turtle.fd(rad)
        turtle.seth(0)
        turtle.fd(rad)
        turtle.seth(angle)
        turtle.fd(rad)
   


main()
