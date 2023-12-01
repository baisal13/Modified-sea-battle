import os
import random

# Function to create an empty game board
def create_empty_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]

# Function to check if a ship can be placed at a given position
def can_place_ship(board, row, col, size, orientation):
    if orientation == 'horizontal':
        for c in range(col, col + size):
            if c >= len(board[0]) or board[row][c] != 'O':
                return False
    else:
        for r in range(row, row + size):
            if r >= len(board) or board[r][col] != 'O':
                return False

    return True

# Function to place ships on the board
def place_ships(board, ship_sizes):
    orientations = ['horizontal', 'vertical']
    for size in ship_sizes:
        while True:
            orientation = random.choice(orientations)
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)

            if (orientation == 'horizontal' and col + size <= len(board[0])) or (orientation == 'vertical' and row + size <= len(board)):
                if can_place_ship(board, row, col, size, orientation):
                    if orientation == 'horizontal':
                        for c in range(col, col + size):
                            board[row][c] = 'X'
                    else:
                        for r in range(row, row + size):
                            board[r][col] = 'X'
                    break

# Function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Ask for the player's name
player_name = input("Enter your name: ")

# Create an empty game board
board_size = 7
game_board = create_empty_board(board_size)

# Place ships on the board
ship_sizes = [3, 2, 2, 1, 1, 1, 1]  # Sizes of ships
place_ships(game_board, ship_sizes)

# Game start
print(f"Hello, {player_name}! Let's play the game!")
print("Your game board:")
print_board(game_board)
# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')





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

# Function to get the player's shot
def get_player_shot():
    while True:
        try:
            shot = input("Enter coordinates to fire (e.g., A1): ")
            if len(shot) < 2 or not shot[0].isalpha() or not shot[1:].isdigit():
                raise ValueError("Invalid input! Enter a letter followed by a number.")
            
            row, col = convert_coordinates(shot)
            if not (0 <= row < 7 and 0 <= col < 7):
                raise ValueError("Coordinates out of bounds! Try again.")

            return row, col
        except ValueError as e:
            print(e)

# Function to update grid after a shot
def update_grid(grid, x, y):
    if grid[x][y] != ".":
        ship_size = int(grid[x][y])
        grid[x][y] = "hit"
        # Check if the ship is sunk
        if all(cell != str(ship_size) for row in grid for cell in row):
            return "sunk"
        return "hit"
    else:
        grid[x][y] = "miss"
        return "miss"


# Function to start the game
def start_game():
    scores = {}
    while True:
        shots = play_game()
        scores[shots] = scores.get(shots, []) + [input("Do you want to play again? (yes/no): ")]
        if scores[shots][-1].lower() != 'yes':
            clear_screen()
            print("Game Over!")
            print("Here are the scores:")
            sorted_scores = sorted(scores.items(), key=lambda x: x[0])
            for score, players in sorted_scores:
                for player in players:
                    print(f"Player: {player}, Shots: {score}")
            break

if __name__ == "__main__":
    start_game()