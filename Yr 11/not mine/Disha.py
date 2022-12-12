from tkinter import *

from tkinter import ttk

from tkinter import scrolledtext

from tkinter.ttk import Combobox

import math



def cost(): 

    scost = int(sdropdown.get()) * 4.2 

    mcost = int(mdropdown.get()) * 5.2

    lcost = int(ldropdown.get()) * 5.8

    cost = mcost + scost + lcost

    costspacelbl.configure(text=(str(cost)))

#create window

window = Tk()

window.title('Coffee App')

window.geometry('500x300')



applbl = Label(window, text='Coffee App', font=('Arial Bold',14))

applbl.focus()

applbl.place(relx = 0.5, rely = 0.09, anchor=CENTER)



slbl = Label(window, text='Small Coffee', font=('Arial Bold italic',12))

slbl.place(relx = 0.15, rely = 0.19, anchor=CENTER)



mlbl = Label(window, text='Medium Coffee', font=('Arial Bold italic',12))

mlbl.place(relx = 0.16, rely = 0.29, anchor=CENTER)



llbl = Label(window, text='Large Coffee', font=('Arial Bold italic', 12))

llbl.place(relx = 0.14, rely = 0.39, anchor=CENTER)



totalcostlbl = Label(window, text='Total Cost', font=('Arial Bold italic', 12))

totalcostlbl.place(relx = 0.16, rely = 0.49, anchor=CENTER)



costspacelbl = Label(window, text=' ')

costspacelbl.place(relx = 0.4, rely = 0.49, anchor=CENTER)



sdropdown = Combobox(window, state='readonly')

sdropdown.set('Select')

sdropdown['values']= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

sdropdown.place(relx=0.45, rely=0.19, anchor=CENTER)



mdropdown = Combobox(window, state='readonly')

mdropdown.set('Select')

mdropdown['values']= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

mdropdown.place(relx=0.45, rely=0.29, anchor=CENTER)



ldropdown = Combobox(window, state='readonly')

ldropdown.set('Select')

ldropdown['values']= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

ldropdown.place(relx=0.45, rely=0.39, anchor=CENTER)



submitbtn = Button(window, text='Submit', command=cost)

submitbtn.place(relx = 0.5, rely = 0.49, anchor=CENTER)



window.mainloop()
