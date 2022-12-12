import math

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
print("      !!!Steve's Coffee Ordering System!!!")
print("\n")
print("      Enter the amount of coffee's ordered")
print("\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                    Prices")
print("\n")
print("  Small - $4.20 , Medium - $5.20 , Large - $5.80 ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




small = input("Small Coffee(s): ")
medium = input("Medium Coffee(s): ")
large = input("Large Coffee(s): ")
small_price = 4.20
medium_price = 5.20
large_price = 5.80
yes_no = input("Do you have a concession card? ")
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

print("\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("         Total amount of coffees ordered")
print("        ---------------------------------")
print("Small Coffees: " + " " + " "  + small)
print("Medium Coffees: " + " " + medium)
print("Large Coffees: " + " " + " " + large)
print("Discount of 20% if answer to having a card was yes")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                 Total Price is")
print('                ----------------')
discount = str(discount1)
print("Total saved (By discount):   "+ "$" + discount)
print("Coffee Total:    $" + total[:5])


