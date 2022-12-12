import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 300
window_height = 300
window = pygame.display.set_mode((window_width, window_height))

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This function draws a line on the screen
def draw_line(start, end):
    pygame.draw.line(window, BLACK, start, end, 5)

# This function draws the Tic Tac Toe board
def draw_board():
    # Draw the vertical lines
    draw_line((100, 0), (100, 300))
    draw_line((200, 0), (200, 300))

    # Draw the horizontal lines
    draw_line((0, 100), (300, 100))
    draw_line((0, 200), (300, 200))

# This function returns the center point of a grid cell
def get_cell_center(i, j):
    return (i * 100 + 50, j * 100 + 50)

# This function draws an X or O in a grid cell
def draw_symbol(i, j, symbol):
    # Get the center point of the cell
    center = get_cell_center(i, j)

    # Draw the symbol
    if symbol == 'X':
        draw_line((center[0] - 25, center[1] - 25), (center[0] + 25, center[1] + 25))
        draw_line((center[0] + 25, center[1] - 25), (center[0] - 25, center[1] + 25))
    elif symbol == 'O':
        pygame.draw.circle(window, BLACK, center, 25)

# This function draws the current state of the game
def draw_game():
    # Clear the window
    window.fill(WHITE)

    # Draw the board
    draw_board()

    # Draw the symbols (X, O)
    for i in range(3):
        for j in range(3):
            symbol = game[i][j]
            if symbol != '':
                draw_symbol(i, j, symbol)

# This function is called when a mouse button is pressed
def on_mouse_button_down(pos):
    # Calculate the grid cell where the click occurred
    i = pos[0] // 100
    j = pos[1] // 100

    # Don't do anything if the cell is already occupied
    if game[i][j] != '':
        return

    # Set the symbol for the current player in the clicked cell
    game[i][j] = player

    # Switch to the other player
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

# This is the main game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
    
