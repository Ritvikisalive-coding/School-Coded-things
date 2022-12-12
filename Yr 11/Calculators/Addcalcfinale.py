from tkinter import *

window = Tk()
window.title('Add Calc')
window.resizable(0,0)
window.geometry('300x100')
#label for input
lbl1 = Label(window, text="First Number:")
lbl1.grid(column=0, row=1)
#label for input
lbl2 = Label(window, text="Seccond Number:")
lbl2.grid(column=0, row=2)
#input number in field
txt1 = Entry(window,width=10)#text box for input
txt1.grid(column=1 , row=1)
txt1.focus()
#input number in field
txt2 = Entry(window,width=10)#text box for input
txt2.grid(column=1 , row=2)
answer = 0
def clicked():
  num1 = float(txt1.get())#asign to num1
  num2 = float(txt2.get())#asign to num2
  answer = num1 + num2#add both numbers
  print(answer)
  lbl3 = Label(window, text="Result: ")
  lbl3.grid(column=1, row=6)
  lbl3.configure(text="Result: "+ str(answer))#add to lable 
btn = Button(window, text="Addition", bg="light grey", fg="black", command=clicked)#run clicked
btn.grid(column=1, row=3)

window.mainloop()