import tkinter

master=tkinter.Tk()
master.title("place() method")
master.geometry("450x350")

button1=tkinter.Button(master, text="button1")
button1.place(x=25, y=100)

button2=tkinter.Button(master, text="button2")
button2.place(x=100, y=25)

button3=tkinter.Button(master, text="button3")
button3.place(x=175, y=100)

master.mainloop()