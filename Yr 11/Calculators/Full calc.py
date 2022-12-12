from tkinter import *
import math
import tkinter

window = Tk()
window.title('Calculator')
window.iconbitmap("C:\\Users\\ritvi\\Downloads\\download__3_-removebg-preview.ico")#remove later when / if you give file to someone else
window.resizable(0,0)
window.geometry('300x100')
window.configure(bg="black")
#label for input
lbl1 = Label(window, text="First Number:", bg="black", fg="white")
lbl1.grid(column=0, row=1)
#label for input
lbl2 = Label(window, text="Seccond Number:", bg="black", fg="white")
lbl2.grid(column=0, row=2)
#input number in field
txt1 = Entry(window,width=10)#text box for input
txt1.grid(column=1 , row=1)
txt1.focus()
#input number in field
txt2 = Entry(window,width=10)#text box for input
txt2.grid(column=1 , row=2)
answer = 0
lbl3 = Label(window, text="Result: ", bg="black", fg="white")
lbl3.place(x=0, y=55)
def add():
  num1 = float(txt1.get())#asign to num1
  num2 = float(txt2.get())#asign to num2
  answer = num1 + num2#add both numbers
  lbl3.configure(text="Result: "+ str(answer))#add to lable 
def minus():
  num1 = float(txt1.get())#asign to num1
  num2 = float(txt2.get())#asign to num2
  answer = num1 - num2#minus both numbers
  lbl3.configure(text="Result: "+ str(answer))#add to lable 
def divide():
  num1 = float(txt1.get())#asign to num1
  num2 = float(txt2.get())#asign to num2
  answer = num1 / num2#divide both numbers
  lbl3.configure(text="Result: "+ str(answer))#add to lable 
def multiply():
  num1 = float(txt1.get())#asign to num1
  num2 = float(txt2.get())#asign to num2
  answer = num1 * num2#mulitply both numbers
  lbl3.configure(text="Result: "+ str(answer))#add to lable 
def Square():
  num1 = float(txt1.get())#asign to num1
  num2 = float(txt2.get())#asign to num2
  answer = num1 + num2#add both numbers
  answer = math.sqrt(answer)    
  answer = str(answer)
  lbl3.configure(text="Result: "+ str(answer))#add to lable 
def clear():
  lbl3.configure(text="Result: ")#add to lable 
  txt1.delete(0,999)
  txt2.delete(0,999)
  txt1.focus()
btn = Button(window, text="+", bg="orange", fg="white", command=add, width=2)#run clicked
btn.place(x = 231, y =0)
btn1 = Button(window, text="-", bg="orange", fg="white", command=minus, width=2)#run clicked
btn1.place(x = 205, y =0)
btn2 = Button(window, text="/", bg="orange", fg="white", command=divide, width=2)#run clicked
btn2.place(x = 231, y =25)
btn3 = Button(window, text="x", bg="orange", fg="white", command=multiply, width=2)#run clicked
btn3.place(x = 205, y =25)
btn5 = Button(window, text="√", bg="orange", fg="white", command=Square, width=2)#run clicked
btn5.place(x = 257, y =0)
btn4 = Button(window, text="AC", bg="orange", fg="white", command=clear, width=2)#run clicked
btn4.place(x = 257, y =25)
window.mainloop()