from tkinter import * #Import tkinter library

import math #import math library

window = Tk() # background for the calc
window.geometry("350x100") #the size of the calc
window.title('Calculator!!') #title
window.configure(bg="light blue") #background colour 

label1 = Label(window,text="First number:", bg="light blue") #text asking for first number
label1.grid(column=0, row=1) #placement of text asking for first number

txt = Entry(window,width = 25) #The box where first num is inserted
txt.grid(column=1, row=1) #the box placement

label2 = Label(window,text="Second number:", bg="light blue") #next text asking for a second number 
label2.grid(column=0, row=2) #placement of text for the 'Second number'

txt2 = Entry(window,width = 25) #box where second number is put
txt2.grid(column=1, row=2) #The placement of the second text box

label3 = Label(window,text="Result:", bg="beige", fg="purple") # foreground and background colour of  third label
label3.grid(column=1, row=5) #The placement of the third label

def added():
  
  Num1 = float(txt.get()) #assign to Num1
  
  Num2 = float(txt2.get()) #Assign to Num2
  
  add = Num1 + Num2 #Adding the two numbers 
  
  label3.configure(text="Result:"+ str(add)) #Add result next to label3
  
but = Button(window, text="+", command= added, bg= "light green", width =2) #adding'add'button

but.grid(column=5, row=1) #placement of button  

def multiply():

  Num1 = float(txt.get()) #assign to Num1
  
  Num2 = float(txt2.get()) #assign to Num2

  answer = Num1 * Num2 #mulitply numbers together

  label3.configure(text="Result: "+ str(answer)) #add to lable

but2 = Button(window, text="x",command=multiply, bg="coral", fg="black",width =2) 

but2.grid(column= 6, row= 2)

def minus():

  Num1 = float(txt.get()) #assign to Num1

  Num2 = float(txt.get()) #assign to Num2

  answer = Num1 - Num2 #minus Num2 from Num1 

  label3.configure(text = "Result: "+ str(answer)) 
 #add to lable 3


but3 = Button(window, text = "-", command= minus, bg= "plum", fg="black", width =2) #adding minus button
but3.grid(column= 6, row= 1) #placement of button

def divide():
  Num1 = float(txt.get()) #assign to Num1

  Num2 = float(txt.get()) #assign to Num2

  answer = Num1 / Num2 #divide numbers

  label3.configure(text="Result: "+ str(answer)) #add to lable 3

but4 = Button(window, text="/", bg="cornflower blue",
fg="black", command=divide, width=2) #run clicked
but4.grid(column= 5, row= 2) #placement of button 4

window.mainloop()