#Try_draw pictures by time and random_20190313
from turtle import *
from time import *
from random import *
def draw_picture(rand, step):
    begin_fill()
    circle(rand, steps = step)
    end_fill()
    write(("The time ot the programer start:",strftime("%Y-%m-%d %H:%M:%S", localtime())), font=("Times", 18, "normal") )
    penup()
    goto(20, 20)
    pendown()
    write(("The time you used:", time_count()), font = ("Times", 18, "normal"))
def time_count():
    start = perf_counter()
    sleep(3.3)
    end = perf_counter()
    time_used = end - start
    return time_used
def design_picture(a, b):
    rand = randint(a, b)
    step = randint(1, 6)
    return rand, step
def main():
    setup(1200, 900, 0, 0)
    color("green", 'red')
    pensize(9)
    rand, step= design_picture(45, 70)
    draw_picture(rand, step)
    
main()
    
    
    
