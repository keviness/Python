# 响应用户事件2018.10.30

from tkinter import *

def processOK():
    
    print("Ok button is clicked")

def processCancel():
    print("Cancel button is clicked")

def main():
    tk = Tk()
    btnOK = Button(tk, text = "OK", fg = "red", command = processOK)
    btnCancel = Button(tk, text = "Cancel", bg = "yellow", command = processCancel)
    btnOK.pack()
    btnCancel.pack()
    tk.mainloop()
