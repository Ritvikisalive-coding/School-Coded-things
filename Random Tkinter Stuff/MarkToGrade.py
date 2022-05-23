from ast import And
from tkinter import *
from tkinter.ttk import Combobox
def clicked():

    score = int(txt.get())

    while True:

        if score >= 91 and score <= 100: 

            answer = 'Outstanding!'

            break

        elif score >= 81 and score < 91: 

            answer = 'Excellent!'

            break

        elif score >= 75 and score < 81: 

            answer = 'Very good!'

            break

        elif score >= 70 and score < 75: 

            answer = 'Good!'

            break

        elif score >= 60 and score < 70: 

            answer = 'Competent.'

            break

        elif score >= 50 and score < 60: 

            answer = 'Satisfactory.'

            break

        elif score <= 50 and score >= 0:

            answer = 'Below standard.'

            break
        else:
            answer = "Not a Valid Mark"
            break

    lbl3.configure(text="Final Grade: "+ answer)

window = Tk()#Tkinter shortened down command 
window.title("School Score Converter")#window app title
window.geometry('400x100')#window size
window.resizable(0,0)#make it so the window is not re sizeable
lbl = Label(window, text="Score Converter", font=("Arial Bold", 16, ))#titlee of app at the top of the window
lbl.grid(column=1 , row=0)
lbl2 = Label(window, text="Enter Mark(%): ", font=("Arial Bold", 12))#Label saying to input mark
lbl2.grid(column=0, row=20)
btn = Button(window, text="Convert", bg="light grey", fg="black", command=clicked)#button to convert number into grade
btn.grid(column=3, row=20)
txt = Entry(window,width=30)#text box for input
txt.grid(column=1 , row=20)
txt.focus()
if txt.get() > str(100):
    print("This score is not valid")
lbl3 = Label(window, text="The Score is: ", font=("Arial Bold", 10))#label at the bottom of the app that says the finale mark
lbl3.grid(column=1, row=40)


window.mainloop()#open the actual app
