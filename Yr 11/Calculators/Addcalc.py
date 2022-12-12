from tkinter import *





window = Tk()
window.title('Add Calc')
window.resizable(0,0)
window.geometry('300x100')
lbl1 = Label(window, text="First Number:")
lbl1.grid(column=0, row=1)
lbl2 = Label(window, text="Seccond Number:")
lbl2.grid(column=0, row=2)
txt1 = Entry(window,width=10)#text box for input
txt1.grid(column=1 , row=1)
txt1.focus()
txt2 = Entry(window,width=10)#text box for input
txt2.grid(column=1 , row=2)
answer = 0
def clicked():
  num1 = float(txt1.get())
  num2 = float(txt2.get())
  answer = num1 + num2
  lbl3 = Label(window, text="Result: ")
  lbl3.grid(column=1, row=6)
  lbl3.configure(text="Result: "+ str(answer))
btn = Button(window, text="Addition", bg="light grey", fg="black", command=clicked)
btn.grid(column=1, row=3)

window.mainloop()