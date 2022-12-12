from tkinter import *
import tkinter

def screen2():
    window = Tk()
    window.title("screen2")
    window.geometry("350x200")
    
    lbl = Label(window, text="Base App", font=('Bold', 19))
    lbl.place(x=120, y= 0)
    window.destroy
    txt = Entry(window,width=30)
    txt.place(x=90 , y=55)
    txt.focus()
    lbl3 = Label(window, text="Hello there ")
    lbl3.place(x=135, y= 145)
    
    window.mainloop()
