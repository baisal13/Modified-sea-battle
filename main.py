import os
import random

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
<<<<<<< HEAD

# Function to print the game grid
def print_grid(grid):
    print("   A B C D E F G")
    for i, row in enumerate(grid):
        print(f"{i + 1} {' '.join(row)}")
    print()
=======
>>>>>>> 30e59d90048319d989a174d55a097d464804b765
