from guesses import MoveTracker, get_player_guess
from duplicates import
from grid_generator import 
from healthbar import

def main():
    print(" ")    
    print("|---------------------------------------------------|")
    print("| <°)))>< Welcome to the RAMA Fishing Game! ><(((°> |")
    print("|---------------------------------------------------|")
    print(" ") 
    print("Catch 5 fish before you run out of health, guesses, or time.")
    print("You have 3 health, 10 guesses, and 2 minutes.\n")
    print(" ")
    print("1. Throw your line!")
    print(" ")
    print("2. Get outta here!")
    print(" ")
    
    option = input("Select 1 or 2 from above: ")
    
    if option == '1':
        print(" ")
        print("---------------------------------")
        print("| Time to go fishin'!   ><(((°> |")
        print("---------------------------------")
        print(" ")
        
        grid = 
        move_tracker = MoveTracker()
        game_state = 
        health_bar = 
        
    elif option == '2':
        print(" ")
        print("See ya!")
        print(" ")
    else:
        raise ValueError("Not a valid option!")
    
    
    
    
move_tracker = MoveTracker(rows=7, columns=7)

while True:
    row, column = get_player_guess(move_tracker)
    
    print(f"You selected row {row + 1}, column {column + 1}")
    
    print(f"Used moves: {move_tracker.used_moves}")
    
    print()
    
if __name__ == "__main__":
    main()