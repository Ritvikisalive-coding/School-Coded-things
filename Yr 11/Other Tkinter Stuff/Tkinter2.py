from tkinter import *
from tkinter.ttk import Combobox

def clicked():

    score = int(txt.get())

    while True:

        if score >= 91 and score < 100: 

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

        else:

            answer = 'Below standard.'

            break

    lbl3.configure(text="Final score: "+ answer)

window = Tk()
window.title("School Score Converter")
window.geometry('400x100')
window.resizable(0,0)
lbl = Label(window, text="Score Converter", font=("Arial Bold", 16, ))
lbl.grid(column=1 , row=0)
lbl2 = Label(window, text="Enter Mark(%): ", font=("Arial Bold", 12))
lbl2.grid(column=0, row=20)
btn = Button(window, text="Convert", bg="light grey", fg="black", command=clicked)
btn.grid(column=3, row=20)
txt = Entry(window,width=30)
txt.grid(column=1 , row=20)
txt.focus()
lbl3 = Label(window, text="The Score is: ", font=("Arial Bold", 12))
lbl3.grid(column=1, row=40)

#combo = Combobox(window)
#combo ['values']= (1, 2, 3, 4, 5, "Text")
#combo.current(1)
#combo.grid(column=0, row=0)
#chk_state = BooleanVar()
#chk_state.set(True)
#chk = Checkbutton(window, text='Choose', var=chk_state)
#chk.grid(column=0, row=0)
#rad1 = Radiobutton(window, text='First', value=1)
#rad2 = Radiobutton(window, text='Second', value=2)
#rad3 = Radiobutton(window, text='Third', value=3)
#rad1.grid(column=0, row=0)
#rad2.grid(column=1, row=0)
#rad3.grid(column=2, row=0)
window.mainloop()
