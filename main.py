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

# Function to play the game
def play_game():
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Let's play Battleship.")

    shots = 0
    game_grid = [["." for _ in range(7)] for _ in range(7)]
    place_ships(game_grid)

    while True:
        clear_screen()
        print("Your grid:")
        print_grid(game_grid)
        
        x, y = get_player_shot()
        
        if game_grid[x][y] == "miss" or game_grid[x][y] == "hit":
            print("You've already shot there! Try again.")
            input("Press Enter to continue...")
            continue

        result = update_grid(game_grid, x, y)
        shots += 1
        
        if result == "sunk":
            clear_screen()
            print("Your grid:")
            print_grid(game_grid)
            print(f"Congratulations! You sank all ships in {shots} shots!")
            break

    return shots

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