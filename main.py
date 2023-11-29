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