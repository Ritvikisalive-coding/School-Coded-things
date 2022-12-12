from tkinter import *

window = Tk()
window.title("Music Player")
window.geometry("300x600")
window.resizable(0,0)
window.configure(bg = "#b0ffc9")
def play():
    Play['state'] = DISABLED

def pause():
    Pause['state'] = DISABLED
def foward():
    print("HELLO")

def back():
    print("HELLO")








lbl = Label(window, text="Music Player",font=('Bold', 19), bg = "#b0ffc9", fg = "#50735b")
lbl.place(x=80,y=10)

#Action buttons
Play = Button(window, text = 'Play', command = play, width = 10, bg = "#50735b", fg = "white")
Pause = Button(window, text = 'Pause', command = pause, width = 10, bg = "#50735b", fg = "white")
Foward = Button(window, text = 'Next', command = foward, width = 10, bg = "#50735b", fg = "white")
Backwards = Button(window, text = 'Back', command = back, width = 10, bg = "#50735b", fg = "white")

Play.place(x=110 ,y=410 )
Pause.place(x=110 , y=490 )
Foward.place(x= 50,y=450 )
Backwards.place(x=170 ,y=450 )
#Volume slider



window.mainloop()