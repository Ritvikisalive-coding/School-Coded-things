from ast import And
import math
from tkinter import *
from tkinter.ttk import Combobox
def clicked():

    num2 = int(txt.get())
    add = math.sqrt(num2)    
    add = str(add)


    lbl3.configure(text="Squared Number: "+ add)

window = Tk()#Tkinter shortened down command 
window.title("Square Root")#window app title
window.geometry('550x100')#window size
window.resizable(0,0)#make it so the window is not re sizeable
lbl = Label(window, text="Square Root Calculator", font=("Arial Bold", 16, ))#titlee of app at the top of the window
lbl.grid(column=1 , row=0)
lbl2 = Label(window, text="Enter number: ", font=("Arial Bold", 12))#Label saying to input mark
lbl2.grid(column=0, row=20)

txt = Entry(window,width=30)#text box for input
txt.grid(column=1 , row=20)
txt.focus()
if txt.get() > str(100):
    print("This score is not valid")
btn = Button(window, text="Root it", bg="light grey", fg="black", command=clicked)#button to convert number into grade
btn.grid(column=2, row=20)
btn = Button(window, text='Delete', command=lambda: txt.delete(0,END))
btn.grid(column=2, row=40)
lbl3 = Label(window, text="Squared Rooted number: ", font=("Arial Bold", 10))#label at the bottom of the app that says the finale mark
lbl3.grid(column=1, row=40)


window.mainloop()#open the actual app
