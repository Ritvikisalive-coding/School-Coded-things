from tkinter import *
from tkinter.ttk import *#For Combobox 

window = Tk()
window.title("Coffee Orderer")
window.geometry("500x500")

lbl = Label(window, text="Coffee Ordering System", font=('Bold', 12))
lbl.place(x=155, y= 0)





lbl1 = Label(window, text="Small Coffee", font=('Bold', 12))
lbl1.place(x = 70 , y = 70)
lbl2 = Label(window, text="Medium Coffee", font=('Bold', 12))
lbl2.place(x = 70 , y = 100)
lbl3 = Label(window, text="Large Coffee", font=('Bold', 12))
lbl3.place(x = 70 , y = 130)

small = StringVar()
medium = StringVar()
large = StringVar()

#Replace with spin box


combo = Combobox(window, textvariable = small, state='readonly')
combo['values']= (0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo.place(x = 200 , y = 70)
combo1 = Combobox(window, textvariable = medium, state='readonly')
combo1['values']= (0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo1.place(x = 200 , y = 100)
combo2 = Combobox(window, textvariable = large, state='readonly')
combo2['values']= (0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combo2.place(x = 200 , y = 130)

small1 = combo.get()
medium2 = combo1.get()
large3 = combo2.get()



#all = "Small: "+ small, "Medium: "+ medium, "Large: "+ large 
#all = str(all)
def hi(): 
    global small1, medium2, large3
    small_price = 4
    medium_price = 5
    large_price = 5
    yes_no = input("Do you have a concession card? ")
    yes_no = yes_no.upper()
    #small_total = small * small_price
    #medium_total = medium * medium_price 
    #large_total = large * large_price

    total = small1 * small_price + medium_price * medium2 + large_price * large3
    

    if yes_no == "YES":
        print("\n")
        print("A 20% Discount has been added")
        print(total + 'hi')
        discount1 = total/5
        print(discount1)
    #discount2 = discount1 * 2
        discount3 = total - discount1
        print(discount3)
        discount = discount3
    else:
        print("\n")
        print("No discount has been added")
        discount = total
        discount1 = 0







btn = Button(window, text="Click Me", command=hi)
btn.place(x=150, y= 400)








window.mainloop()
