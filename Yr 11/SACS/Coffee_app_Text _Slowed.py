import math
from time import sleep

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
sleep(1.2)
print("\n")
print("      !!!Steve's Coffee Ordering System!!!")
sleep(1.2)
print("\n")
print("      Enter the amount of coffee's ordered")
sleep(1.2)
print("\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
sleep(1.2)
print("                    Prices")
sleep(1.2)
print("\n")
print("  Small - $4.20 , Medium - $5.20 , Large - $5.80 ")
sleep(1.2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



sleep(1)
small = input("Small Coffee(s): ")
sleep(0.2)
medium = input("Medium Coffee(s): ")
sleep(0.3)
large = input("Large Coffee(s): ")
sleep(0.4)
small_price = 4.20
medium_price = 5.20
large_price = 5.80
yes_no = input("Do you have a concession card? ")
sleep(0.9)
yes_no = yes_no.upper()


small1 = int(small)
medium1 = int(medium)
large1 = int(large)



small_total = small1 * small_price
medium_total = medium1 * medium_price 
large_total = large1 * large_price

total = small_total + medium_total + large_total
#total = int(total)

if yes_no == "YES":
    print("\n")
    print("A 20% Discount has been added")
    discount1 = total/5
    #discount2 = discount1 * 2
    discount3 = total - discount1
    discount = discount3
else:
    print("\n")
    print("No discount has been added")
    discount = total
    discount1 = 0
total = discount
total = str(total)
sleep(3)
print("\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
sleep(3)
print("         Total amount of coffees ordered")
sleep(3)
print("        ---------------------------------")
sleep(3)
print("Small Coffees: " + " " + " "  + small)
sleep(3)
print("Medium Coffees: " + " " + medium)
sleep(3)
print("Large Coffees: " + " " + " " + large)
sleep(3)
print("Discount of 20% if answer to having a card was yes")
sleep(3)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
sleep(3)
print("              Total Price is")
sleep(3)
print('             ----------------')
sleep(3)
discount = str(discount1)
print("Total saved (By discount):   "+ "$" + discount)
sleep(4)
print("Coffee Total:    $" + total[:5])
sleep(3)

