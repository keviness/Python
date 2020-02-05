import turtle
def main():
    turtle.setup(1300, 800, 1, 2)

    pythonsize = 9
    
    turtle.pensize(pythonsize)
    turtle.color('blue')

    draw(20, 120)
    
def draw(rad, angle):

    turtle.seth(0)
    turtle.fd(100)
    turtle.seth(120)
    turtle.fd(100)
    turtle.seth(-120)
    turtle.fd(100)
main()
