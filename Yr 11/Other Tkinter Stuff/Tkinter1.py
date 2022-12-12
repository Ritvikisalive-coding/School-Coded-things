from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from os import path




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Base of the tkinter application
window = Tk()
window.title('Welcome to applied computing')
window.geometry('600x700')
#End of Base
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Label Widgets
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=1)
#End of Label
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Label Widgets(Font)
lbl = Label(window, text="Hello",font=("CourierNew"))
lbl.grid(column=0, row=2)
#End of Label
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Label Widgets(Size)
lbl = Label(window, text="Hello", font=("CourierNew", 19))
lbl.grid(column=0, row=3)
#End of Label
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Button Widgets
btn = tkinter.Button(window, text="click me")
btn.grid(column=0, row=4)
#End of Button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Button Widgets(Text Colour)
btn1 = tkinter.Button(window, text="huuuuuuuu",fg="red" )
btn1.grid(column=0, row=5)
#End of Button

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Button Widgets(Button Colour)
btn2 = tkinter.Button(window, text="hu", bg="blue")
btn2.grid(column=0, row=6)
#End of Button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Text Field Widget
txt = Entry(window,width=30)#text box for input
txt.grid(column=0 , row=20)
txt.focus()
#End of text field
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Radio Button
rad1 = Radiobutton(window,text='SUP', value=1)
rad1.grid(column=0 , row=21)
#End of Radio Button
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter App Window Tabs
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.grid(column=0 , row=0)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')

tab_control.add(tab2, text='Second')

lbl1 = Label(tab1, text= 'label1')

lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text= 'label2')

lbl2.grid(column=0, row=0)

tab_control.grid(column=0 , row=0)
#End of Window Tabs
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Menu Bar
menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')
new_item.add_command(label='You')
new_item.add_command(label='Are')
new_item.add_command(label='So')
new_item.add_command(label='Gay')

menu1 = Menu(window)

new_item1 = Menu(menu)

new_item1.add_command(label='New')

new_item1.add_separator()

new_item1.add_command(label='Edit')

menu.add_cascade(label='Save', menu=new_item1)

window.config(menu=menu)


menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)
#End of Tkinter Menu Bar
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#'''Open File Explorer(Save File)
def file1():
    file = filedialog.asksaveasfile(filetypes = (("Text files","*.txt"),("all files","*.*")))

btn = Button(window, text="Save", command = file1)
btn.grid(column=0, row=8)
#end of file explorer'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#'''Open File Explorer (Open File)
def file1():
    file = filedialog.askopenfile(filetypes = (("Text files","*.txt"),("all files","*.*")))

btn = Button(window, text="Open", command = file1)
btn.grid(column=0, row=9)
#end of file explorer'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Tkinter Combobox (Drop down selection)
combo = Combobox(window)
combo['values']= (" ",1, 2, 3, 4, 5, "Text")
combo.current(0)
combo.grid(column=0, row=10)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Check Boxes
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=11)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#check Box check state
chk_state = IntVar()
chk_state.set(0) #uncheck
chk_state.set(1) #check
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Radio Button Retrival
selected = IntVar()
def clicked():
   print(selected.get())
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=12)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Scroll Bar text field
txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column=0,row=13)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Set Scroll Bar text field content
txt.insert(INSERT,'You text goes here')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Delete Text in Scroll Bar Text Field
def clickeds():
    txt.delete(1.0,END)
btn = Button(window, text="Clear", command=clickeds)
btn.grid(column=0, row=14)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Message Box(+Errors & Warning Messages)
def clicked3():
    messagebox.showinfo('Message title', 'Message content')
    messagebox.showwarning('Message title', 'Message content')  #shows warning message
    messagebox.showerror('Message title', 'Message content')    #shows error message
btn = Button(window,text='Pop Up Error Box', command=clicked3)
btn.grid(column=0,row=15)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#askquestion dialog
def clicked4():
    res = messagebox.askquestion('Message title','Message content')
    res = messagebox.askyesno('Message title','Message content')
    res = messagebox.askyesnocancel('Message title','Message content')
    res = messagebox.askokcancel('Message title','Message content')
    res = messagebox.askretrycancel('Message title','Message content')
btn = Button(window,text='Question Boxs', command=clicked4)
btn.grid(column=0,row=16)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Spin Box
spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0,row=17)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Progress Bar
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 25
bar.grid(column=0, row=18)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Ask For Directory in file explorer
def file2():
    dir = filedialog.askdirectory()#Open Directory
    file = filedialog.askopenfilename(initialdir= path.dirname(__file__))#Open FILE

btn = Button(window, text="Filething", command = file2)
btn.grid(column=0, row=19)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

























window.mainloop()