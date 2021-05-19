# control the photo move 2018.11.2.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()

def moverectangle(event):
    if event.keysym == "Up":
        canvas.move(1, 0, -5)
    elif event.keysym == "Down":
        canvas.move(1, 0, 5)
    elif event.keysym == "Left":
        canvas.move(1, -5, 0)
    elif event.keysym == "Right":
        canvas.move(1, 5, 0)


canvas.create_rectangle(14, 15, 9, 10, fill = "blue")
canvas.bind_all("<KeyPress-Up>", moverectangle)
canvas.bind_all("<KeyPress-Down>", moverectangle)
canvas.bind_all("<KeyPress-Left>", moverectangle)
canvas.bind_all("<KeyPress-Right>", moverectangle)
    
