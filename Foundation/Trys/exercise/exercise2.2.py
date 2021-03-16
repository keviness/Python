import turtle

def main():

    turtle.setup(1200, 800, 0, 0)

    pythonsize = 10
    turtle.pensize(pythonsize)

   

    draw(250, 60)

def draw(width, rad):

    
    turtle.seth(rad)
    turtle.fd(width)
    turtle.seth(-rad)
    turtle.fd(width)
    turtle.seth(180)
    turtle.fd(width)
    

main()
