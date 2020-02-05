# try Tkinter import2018.10.30

from tkinter import *

tk = Tk()
label = Label(tk, text="welcome to Python Tkinter")
button = Button(tk, text ="Click Me")

label.pack()
button.pack()
tk.manloop()
