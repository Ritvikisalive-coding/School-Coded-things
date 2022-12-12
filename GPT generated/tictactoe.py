import tkinter

# Create the main window
window = tkinter.Tk()

# Create a 3x3 grid of buttons for the Tic Tac Toe board
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tkinter.Button(window, width=5, height=5)
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Keep track of whose turn it is (X goes first)
turn = 'X'

# Create a function that will be called when a button is clicked
def on_button_click(i, j):
    global turn

    # Set the text of the button that was clicked
    buttons[i][j].config(text=turn)

    # Alternate between 'X' and 'O' for each turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

# Bind the on_button_click function to each button's 'clicked' event
for i in range(3):
    for j in range(3):
        buttons[i][j].bind('<Button-1>', lambda e, i=i, j=j: on_button_click(i, j))

# Start the event loop to display the window
window.mainloop()
