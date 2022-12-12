from tkinter import *
from time import sleep
window = Tk()
window.title("App Base")
window.geometry("350x200")

lbl = Label(window, text="What is Disha?", font=('Bold', 19))
lbl.place(x=120, y= 0)

txt = Entry(window,width=30)
txt.place(x=90 , y=55)
txt.focus()
lbl3 = Label(window, text="Hello there ")
lbl3.place(x=135, y= 145)
def clicked():
    btn['state'] = DISABLED
    txt['state'] = DISABLED

    res = "Hello there " + txt.get()
    lbl3.configure(text= res)
def reset(): #resetting the output and cost variable
    btn ['state'] = NORMAL
    txt ['state'] = NORMAL

    res = "Hello there " + " "
    lbl3.configure(text= res)
btn = Button(window, text="ClickMe", command=clicked)
btn.place(x=150, y= 100)
Reset = Button(window, text = 'Reset', command = reset)
Reset.place(x = 75, y = 100)
window.mainloop()
