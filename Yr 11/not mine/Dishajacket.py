from tkinter import *

from tkinter import ttk

from tkinter import scrolledtext

from tkinter.ttk import Combobox

import math



def autoupdate(*args):

    with open('info.txt', 'w') as f: 

        f.write(entryvar.get() + '\n')

        f.write(entryvar2.get()+ '\n')

        f.write(entryvar3.get()+ '\n')

        f.write(entryvar4.get()+ '\n')

        f.write(entryvar5.get())



#create window

window = Tk()

window.title('Custom Jacket Orders')

window.geometry('500x400')



#create tabs

tabcontrol = ttk.Notebook(window)

maintab = ttk.Frame(tabcontrol)

tabcontrol.add(maintab, text='main')

tabcontrol.pack(expand=1, fill='both')



#combobox dropdown

entryvar3 = StringVar()

sdropdown = Combobox(window, state='readonly', textvariable= entryvar3)

sdropdown.set('Select a size')

sdropdown['values']= ('XS', 'S', 'M', 'L', 'XL', 'XXL')

sdropdown.place(relx=0.275, rely=0.3, anchor=CENTER)



#combobox dropdown 2

entryvar5 = StringVar()

cdropdown = Combobox(window, state='readonly', textvariable= entryvar5)

cdropdown.set('Choose a colour')

cdropdown['values']= ('Red', 'Blue', 'White')

cdropdown.place(relx=0.425, rely=0.5, anchor=CENTER)



#?maybe radiobutton menu



#labels

namelbl = Label(window, text='Name:', font=('Arial Bold',13))

namelbl.place(relx=0.1, rely=0.1, anchor=CENTER)

schoollbl = Label(window, text='School Code:', font=('Arial Bold', 13))

schoollbl.place(relx=0.15, rely=0.2, anchor=CENTER)

sizelbl = Label(window, text='Size:', font=('Arial Bold', 13))

sizelbl.place(relx=0.081, rely=0.3, anchor=CENTER)

custxtlbl = Label(window, text='Custom Text:', font=('Arial Bold', 13))

custxtlbl.place(relx=0.15, rely=0.4, anchor=CENTER)

colourlbl = Label(window, text='Jacket Colour:', font=('Arial Bold', 13))

colourlbl.place(relx = 0.155, rely=0.5, anchor=CENTER)



#input tabs

entryvar = StringVar()

ninpt = Entry(window, width=15, textvariable=entryvar)

ninpt.focus()

ninpt.place(relx=0.25, rely=0.1, anchor=CENTER)

entryvar2 = StringVar()

scinpt = Entry(window, width=15, textvariable=entryvar2)

scinpt.focus()

scinpt.place(relx=0.36, rely=0.2, anchor=CENTER)

entryvar4 = StringVar()

ctinpt = Entry(window, width=15, textvariable=entryvar4)

ctinpt.focus()

ctinpt.place(relx=0.36, rely=0.4, anchor=CENTER)

#if len(entryvar4.get()) > 12: 

    #entryvar4.delete(12, END)



#trace inputs

entryvar.trace('w', autoupdate)

entryvar2.trace('w', autoupdate)

entryvar3.trace('w', autoupdate)

entryvar4.trace('w', autoupdate) 

entryvar5.trace('w', autoupdate)



#button to add suborder

subbtn = Button(maintab, text='Add a sub-order')

subbtn.place(relx = 0.14, rely= 0.6, anchor=CENTER)



count = 0

#scrolled text window

stwindow = scrolledtext.ScrolledText(window, width=20, height=14, font =('Times New Roman',11))

stwindow.place(relx=0.83, rely=0.375, anchor=CENTER)

stwindow.insert(INSERT, 'Order ' + str(count))

stwindow.configure(state=DISABLED)

stwindow.tag_nextrange



#test to read file in console

with open('info.txt', 'r') as r: 

    print(r.read())







window.mainloop()