from tkinter import *
from tkinter import filedialog#For file explorer


window = Tk()
window.geometry("200x160")
window.resizable(0,0)
window.configure(bg = "Black")


def file1():
    file = filedialog.asksaveasfile(initialfile='Untitled.txt', defaultextension='.txt',filetypes = (("Text files","*.txt"),("all files","*.*")))
def file2():
    file = filedialog.askopenfile(initialfile='Untitled.txt', defaultextension='.txt',filetypes = (("Text files","*.txt"),("all files","*.*")))
def clicked():
	lbl2.configure(text ="Hello There " + " "+ txt.get())



lbl = Label(window,text="Welcome Generator", bg = "Black", fg = "White")
lbl.place(x=43, y=20)
lbl3 = Label(window,text="Please Enter Name", bg = "Black", fg = "red")
lbl3.place(x=45, y=36)
txt = Entry(window, width = 20)
txt.place(x = 37 , y = 60)
btn = Button(window, text= "Convert", command = clicked)
btn.place(x = 74 , y = 100)
lbl2 = Label(window,text="Hello There  ", bg = "Black", fg = "White")
lbl2.place(x=50, y=130)


menu=Menu(window)

menu1 = Menu(window)
new_item1 = Menu(menu)
new_item2 = Menu(menu)
new_item3 = Menu(menu)
new_item1.add_command(label='Exit', command = window.quit)
new_item1.add_command(label='Save (W.I.P)', command = file1)
new_item2.add_command(label='Exit', command = window.quit)
new_item3.add_command(label='Exit', command = window.quit)
new_item3.add_command(label='Open(W.I.P)', command = file2)
menu.add_cascade(label='File', menu=new_item1)
menu.add_cascade(label='Open', menu=new_item3)
menu.add_cascade(label='Exit', menu=new_item2)
window.config(menu=menu)


window.mainloop()