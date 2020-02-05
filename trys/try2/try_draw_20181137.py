# try draw-20181127.py
from turtle import * 
def main():
    
    setup(1000, 900, 0, 0)
    color("red", 'green')
    pensize(10)
    draw(50, 145)
    
def draw(rad, angle):
	
	for i in range(5):
		    fd(rad)
		    left(angle)

    
main()
