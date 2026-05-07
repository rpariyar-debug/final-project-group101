from guesses import MoveTracker, get_player_guess
from duplicates import
from grid_generator import 
from healthbar import

def main():
    print("Welcome to the Fishing Game!")
    print("Catch 5 fish before you run out of health, guesses, or time.")
    print("You have 3 health, 10 guesses, and 2 minutes.\n")
    
    grid = 
    move_tracker = MoveTracker()
    game_state = 
    health_bar = 
    
    
    
move_tracker = MoveTracker(rows=7, columns=7)

while True:
    row, column = get_player_guess(move_tracker)
    
    print(f"You selected row {row + 1}, column {column + 1}")
    
    print(f"Used moves: {move_tracker.used_moves}")
    
    print()
    
if __name__ == "__main__":
    main()