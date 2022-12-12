from tkinter import *
from Screen2 import screen2

def login():
    window = Tk()
    window.title("App Base")
    window.geometry("350x200")
    
    lbl = Label(window, text="Base App", font=('Bold', 19))
    lbl.place(x=120, y= 0)

    def clicked():
        global screen2
        window.destroy
        screen2 = screen2()
        
    
    txt = Entry(window,width=30)
    txt.place(x=90 , y=55)
    txt.focus()
    lbl3 = Label(window, text="Hello there ")
    lbl3.place(x=135, y= 145)
    btn = Button(window, text="Click Me", command=clicked)
    btn.place(x=150, y= 100)
    window.mainloop()
login()
