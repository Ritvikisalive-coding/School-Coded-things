from tkinter import *





window = Tk()
window.title('Jacket Ordering System')
window.geometry('600x500')
lbl = Label(window, text="GWSC Year Jacket Ordering System", font=('Bold', 19))
lbl.place(x=70 , y=25)
var1 = IntVar()
lbl1 = Label(window, text="Order Saved", font=('Helvetica', 15))
lbl1.place(x=235 , y=440)











lbl2 = Label(window, text="Name", font=('Helvetica', 15))
lbl2.place(x=85 , y=120)
lbl3 = Label(window, text="Student ID", font=('Helvetica', 15))
lbl3.place(x=85 , y=175)
lbl4 = Label(window, text="Size", font=('Helvetica', 15))
lbl4.place(x=85 , y=230)
lbl5 = Label(window, text="Text", font=('Helvetica', 15))
lbl5.place(x=85 , y=283)

name1 = Entry(window,width=30)
name1.place(x=200 , y=120)
name1.focus()
id2 = Entry(window,width=30)
id2.place(x=200 , y=175)
id2.focus()
rad1 = Radiobutton(window,text='XS', value=1, variable = var1)
rad2 = Radiobutton(window,text='S', value=2, variable = var1)
rad3 = Radiobutton(window,text='M', value=3, variable = var1)
rad4 = Radiobutton(window,text='L', value=4, variable = var1)
rad5 = Radiobutton(window,text='XL', value=5, variable = var1)
Size = var1.get()
rad1.place(x=200 , y=230)
rad2.place(x=240 , y=230)
rad3.place(x=280 , y=230)
rad4.place(x=320 , y=230)
rad5.place(x=355 , y=230)
txt = Entry(window,width=30)
txt.place(x=200 , y=283)
txt.focus()
name = name1.get()
id = id2.get()
id3 = str(id)
text = txt.get()
file_name = "student_jackets.csv"
data = [name, id3, Size, text]
i = 0
def clicked():
    f = open(file_name,'a')
    for i in range(len(data)):
      if i != 0: 
        f.write(",")
      f.writelines(data[1])
    f.write("\n")
    f.close()
lbl1.configure(text= name1.get() + "Order Saved")
clicked()
btn1 = Button(window, text="Order Now", width= 12, fg="#1D3161" , bg="#F02F28",font=('Helvetica', 19), command=clicked)
btn1.place(x=200 , y=360)






Exit = Button(window, text = 'Exit', width= 12, fg="Hot Pink" , bg="Light Grey", command = window.quit)
Exit.place(x = 500, y = 459)

if len(id)> 7:
    print("Student Code is longer then 7 characters")
    id = id[:7]

if len(text)> 15:
  print("Text is longer then 15 characters")
  text = text[:15]



# Open the file in read mode, read one line and print it
f = open("student_jackets.csv",'r')
try:
   
    print(f.readline())
finally:
    f.close()

# Open a new file, write data to it and then









window.mainloop()