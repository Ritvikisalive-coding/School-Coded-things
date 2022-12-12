from tkinter import *
import tkinter
from screen2 import screen2funt

def login():
    window = Tk()
    root = tkinter.Tk()
    window.title("App Base")
    window.geometry("350x200")
    
    lbl = Label(window, text="Base App", font=('Bold', 19))
    lbl.place(x=120, y= 0)

    def clicked():
        

    txt = Entry(window,width=30)
    txt.place(x=90 , y=55)
    txt.focus()
    lbl3 = Label(window, text="Hello there ")
    lbl3.place(x=135, y= 145)
    btn = Button(window, text="Click Me", command=clicked)
    btn.place(x=150, y= 100)
    btn2 = Button(window, text="WINDOW BOIIIIIII", command=WINDOW)
    btn2.place(x=150, y= 150)
    window.mainloop()
