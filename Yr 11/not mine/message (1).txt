import tkinter
from tkinter import messagebox
from tkinter import *

rootwindow = Tk()
rootwindow.title('Ice Cream')
rootwindow.geometry('300x250')
#variables
vacost = 1.00
strawcost = 1.25
chococost = 1.50
vatopcost = 0.25
strawtopcost = 0.50
chocotopcost = 0.75
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
cost = float(0.0)
#RadioButtons
Vanila = Radiobutton(rootwindow, text = 'Vanila', variable = var1, value = 1,)
Vanila.place(x = 20, y = 10)
Straw = Radiobutton(rootwindow, text = 'Strawberry', variable = var1, value = 2)
Straw.place(x = 20, y = 35)
Choco = Radiobutton(rootwindow, text = 'Chocolate', variable = var1, value = 3)
Choco.place(x = 20, y = 60)
#CheckBoxes
VanilaTop = Checkbutton(rootwindow, text = 'Vanila', variable = var2, onvalue = 1, offvalue = 0)
VanilaTop.place(x = 150,y = 10)
StrawTop = Checkbutton(rootwindow, text = 'Strawberry', variable = var3, onvalue = 2, offvalue = 0)
StrawTop.place(x = 150,y = 35)
ChocoTop = Checkbutton(rootwindow, text = 'Chocolate', variable = var4, onvalue = 3, offvalue = 0)
ChocoTop.place(x = 150,y = 60)

def calculate(): #Cost calculate function
    global cost, totaldis #getting varibles
    num1 = var1.get()
    num2 = var2.get()
    num3 = var3.get()
    num4 = var4.get()

    Calculate['state'] = DISABLED

    if num1 == 1 and num2 == 1 and num3 == 0 and num4 == 0: #Cost calculation with Vanilla flavour and toppings
        cost = vacost + vatopcost
    elif num1 == 1 and num2 == 0 and num3 == 2 and num4 == 0:
        cost = vacost + strawtopcost
    elif num1 == 1 and num2 == 0 and num3 == 0 and num4 == 3:
        cost = vacost + chocotopcost
    elif num1 == 1 and num2 == 1 and num3 == 2 and num4 == 0:
        cost = vacost + vatopcost + strawtopcost
    elif num1 == 1 and num2 == 1 and num3 == 0 and num4 == 3:
        cost = vacost + vatopcost + chocotopcost
    elif num1 == 1 and num2 == 0 and num3 == 2 and num4 == 3:
        cost = vacost + strawtopcost + chocotopcost
    elif num1 == 1 and num2 == 1 and num3 == 2 and num4 == 3:
        cost = vacost + vatopcost + strawtopcost + chocotopcost
    elif num1 == 2 and num2 == 1 and num3 == 0 and num4 == 0: #Cost calculation with Strawberry flavour and toppings
        cost = strawcost + vatopcost
    elif num1 == 2 and num2 == 0 and num3 == 2 and num4 == 0:
        cost = strawcost + strawtopcost
    elif num1 == 2 and num2 == 0 and num3 == 0 and num4 == 3:
        cost = strawcost + chocotopcost
    elif num1 == 2 and num2 == 1 and num3 == 2 and num4 == 0:
        cost = strawcost + vatopcost + strawtopcost
    elif num1 == 2 and num2 == 1 and num3 == 0 and num4 == 3:
        cost = strawcost + vatopcost + chocotopcost
    elif num1 == 2 and num2 == 0 and num3 == 2 and num4 == 3:
        cost = strawcost + strawtopcost + chocotopcost
    elif num1 == 2 and num2 == 1 and num3 == 2 and num4 == 3:
        cost = strawcost + vatopcost + strawtopcost + chocotopcost
    elif num1 == 3 and num2 == 1 and num3 == 0 and num4 == 0: #Cost calculation with Chocolate flavour and toppings
        cost = chococost + vatopcost
    elif num1 == 3 and num2 == 0 and num3 == 2 and num4 == 0:
        cost = chococost + strawtopcost
    elif num1 == 3 and num2 == 0 and num3 == 0 and num4 == 3:
        cost = chococost + chocotopcost
    elif num1 == 3 and num2 == 1 and num3 == 2 and num4 == 0:
        cost = chococost + vatopcost + strawtopcost
    elif num1 == 3 and num2 == 1 and num3 == 0 and num4 == 3:
        cost = chococost + vatopcost + chocotopcost
    elif num1 == 3 and num2 == 0 and num3 == 2 and num4 == 3:
        cost = chococost + strawtopcost + chocotopcost
    elif num1 == 3 and num2 == 1 and num3 == 2 and num4 == 3:
        cost = chococost + vatopcost + strawtopcost + chocotopcost
    
    totaldis = Label(rootwindow, text = cost, bg = 'white', fg = 'black')
    totaldis.place(x = 200, y = 105)
    print(cost)

def reset(): #resetting the output and cost variable
    cost = 0
    totaldis.destroy()
    Calculate ['state'] = NORMAL

#labels
total = Label(rootwindow, text = 'Total: ',)
total.place(x = 160, y = 105)
display = Label(rootwindow, text = '', bg = 'white')
display.place(x= 200, y = 105)
#CalculateButton
Calculate = Button(rootwindow, text = 'Calculate', command = calculate)
Calculate.place(x = 5, y = 100)
#ResetButton
Reset = Button(rootwindow, text = 'Reset', command = reset)
Reset.place(x = 75, y = 100)
#ExitButton
Exit = Button(rootwindow, text = 'Exit', command = rootwindow.quit)
Exit.place(x = 125, y = 100)

rootwindow.mainloop()