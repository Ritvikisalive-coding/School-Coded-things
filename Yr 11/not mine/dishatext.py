import math
scost = 0
mcost = 0
lcost = 0
cost = 0
answer = ' '

print('Welcome! Here are some coffee prices:') 
print('Small: $4.20' + '\n' + 'Medium: $5.20' + '\n' + 'Large: $5.80') 

while answer!= 'n': 
    size = input('What size coffee would you like (S,M,L)? ')
    number = int(input(f'How many {size} coffees would you like? '))
    cont = input('Do you want to add (Y/N)? ')
    if size.lower() == 's': 
        scost = number * 4.2
    if size.lower() == 'm':
        mcost = number * 5.2
    if size.lower() == 'l': 
        lcost = number * 5.8

#total cost
    cost = scost + mcost + lcost
    with open('coffee.txt', 'a') as c: 
        c.write('Size:' + size + ', ' + 'Amount:' + str(number) + '\n')
    number += number
    if cont.lower() == 'n': 
        answer = 'n'
        card = input('Do you have a concession card? ')
        if card.lower() == 'y': 
            cost = cost * 0.8
        elif card.lower() == 'n': 
            print('No discount added.')
        if card.lower() == 'y':
            cost = cost * 0.8
        with open('coffee.txt', 'a') as c:
            c.write('Total Cost: $' + str(round(cost, 2)))
        with open('coffee.txt', 'r') as r:
            print('Here is your order:' + '\n' + r.read())
        with open('coffee.txt', 'w') as w:
            w.truncate()

