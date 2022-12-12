import tkinter

root = tkinter.Tk()
root.eval('tk::PlaceWindow . center')
def clicked():
    second_win = tkinter.Toplevel(root)
    root.eval(f'tk::PlaceWindow {str(second_win)} center')
btn = Button.tkinter(window, text="Click Me", command=clicked)
btn.place(x=150, y= 100)
root.mainloop()

