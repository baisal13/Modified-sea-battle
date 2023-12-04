import os
import random

# Function to create an empty 7x7 board
def create_board():
    return [['O' for _ in range(7)] for _ in range(7)]

# Function to display the board
def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("   A B C D E F G")
    print("  ---------------")
    for i in range(7):
        print(i + 1, "|", " ".join(board[i]))
    print("\n")

# Function to check if ship placement is valid
def is_valid(board, ship, x, y):
    ship_x, ship_y = len(ship), 1
    for i in range(ship_x):
        for j in range(ship_y):
            if x + i >= 7 or y + j >= 7 or board[x + i][y + j] != 'O':
                return False
    return True

# Function to place ships on the board without touching each other
def place_ships(board):
    ships = [[3], [2, 2], [1, 1, 1, 1]]
    for ship in ships:
        for size in ship:
            placed = False
            while not placed:
                x = random.randint(0, 6)
                y = random.randint(0, 6)
                if random.choice([True, False]):
                    if is_valid(board, ship, x, y):
                        for i in range(size):
                            board[x + i][y] = str(size)
                        placed = True
                else:
                    if is_valid(board, ship, y, x):
                        for i in range(size):
                            board[y + i][x] = str(size)
                        placed = True
    return board

# Function to convert input coordinates to indices
def convert_input(input_coord):
    row = int(input_coord[1]) - 1
    col = ord(input_coord[0].upper()) - ord('A')
    return row, col

# Function to check if the shot hits a ship
def check_shot(board, x, y):
    if board[x][y] != 'O':
        size = int(board[x][y])
        board[x][y] = 'X'
        if all('X' in row for row in board for cell in row if cell == str(size)):
            return f"Hit! You sunk a ship of size {size}!"
        return "Hit!"
    else:
        board[x][y] = '-'
        return "Miss!"

# Main game function
def play_game():
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}!")
    while True:
        board = create_board()
        board = place_ships(board)
        shots = 0
        shot_cells = set()
        while any(str(size) in row for row in board for size in range(1, 4)):
            display_board(board)
            shot = input("Enter coordinates to shoot (e.g., A5): ")
            if len(shot) != 2 or not shot[0].isalpha() or not shot[1].isdigit():
                print("Invalid input! Please enter coordinates like 'A5'.")
                continue
            row, col = convert_input(shot)
            if not (0 <= row < 7 and 0 <= col < 7):
                print("Coordinates are out of bounds! Try again.")
                continue
            if (row, col) in shot_cells:
                print("You've already shot there! Try again.")
                continue
            result = check_shot(board, row, col)
            print(result)
            shots += 1
            shot_cells.add((row, col))

        display_board(board)
        print(f"Congratulations, {player_name}! You won in {shots} shots!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game Over!")

# Run the game
if __name__ == "__main__":
    play_game()