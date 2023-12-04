import os
import random

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the game grid
def print_grid(grid):
    print("   A B C D E F G")
    for i, row in enumerate(grid):
        print(f"{i + 1} {' '.join(row)}")
    print()

# Function to place ships on the grid
def place_ships(grid):
    ships = [[3], [2, 2], [1, 1, 1, 1]]

    for ship in ships:
        ship_placed = False
        while not ship_placed:
            x = random.randint(0, 6)
            y = random.randint(0, 6)
            orientation = random.choice(["horizontal", "vertical"])

            if orientation == "horizontal":
                if is_valid_placement(grid, ship, x, y, orientation):
                    for i in range(len(ship)):
                        grid[x][y + i] = str(ship[i])
                    ship_placed = True
            else:  # vertical
                if is_valid_placement(grid, ship, x, y, orientation):
                    for i in range(len(ship)):
                        grid[x + i][y] = str(ship[i])
                    ship_placed = True

# Function to check if ship placement is valid
def is_valid_placement(grid, ship, x, y, orientation):
    ship_size = len(ship)
    if orientation == "horizontal":
        for i in range(ship_size):
            if y + i >= 7 or grid[x][y + i] != ".":
                return False
    else:  # vertical
        for i in range(ship_size):
            if x + i >= 7 or grid[x + i][y] != ".":
                return False
    return True

# Function to convert coordinates (letter, number) to grid indices
def convert_coordinates(coord):
    col = ord(coord[0].upper()) - ord('A')
    row = int(coord[1:]) - 1
    return row, col

