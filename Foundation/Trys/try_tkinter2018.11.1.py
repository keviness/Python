# 显示文字、图形绘图.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 200, height = 200)
canvas.pack()
canvas.create_text(100, 40, text = "welcome !", fill = "blue", font = ("Times", 16))
myImage = PhotoImage(file = "python_logo.gif")

canvas.create_image(10, 70, anchor = NW, image = myImage)
canvas.create_rectangle(10, 70, 190, 130)

tk.mainloop()
