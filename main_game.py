import time

from guesses import MoveTracker, get_player_guess
from grid_generator import generate_grid, print_grid, place_fish, place_items
from healthbar import Outcomes


def main():
    # Main menu for game, containing user input for starting game which loads grid
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
        
        hidden_grid = generate_grid(7, 7)
        place_fish(hidden_grid, 5)
        place_items(hidden_grid, "B", 5)
        place_items(hidden_grid, "H", 3)
        place_items(hidden_grid, "J", 5)

        visible_grid = generate_grid(7, 7)

        move_tracker = MoveTracker(rows=7, columns=7)

        health_bar = Outcomes(health=3, max_health=3)

        fish_caught = 0
        max_fish = 5
        max_guesses = 10
        time_limit = 120
        start_time = time.time()
        
        while True:
            time_used = time.time() - start_time
            time_left = int(time_limit - time_used)

            if time_left <= 0:
                print("Time is up! Game over.")
                break

            if move_tracker.guesses_left(max_guesses) <= 0:
                print("You ran out of guesses! Game over.")
                break

            if health_bar.health <= 0:
                print("You ran out of health! Game over.")
                break

            if fish_caught >= max_fish:
                print("You caught all 5 fish! You win!")
                break

            print_grid(visible_grid)

            health_bar.print_health()
            print(f"Fish caught: {fish_caught}/{max_fish}")
            print(f"Guesses left: {move_tracker.guesses_left(max_guesses)}")
            print(f"Time left: {time_left} seconds")
            print()

            row, column = get_player_guess(move_tracker)

            hidden_value = hidden_grid[row][column]

            if hidden_value == "F":
                fish_caught += 1
                print("You caught a fish!")
                visible_grid[row][column] = "F"

            elif hidden_value == "B":
                health_bar.status_health("B")
                visible_grid[row][column] = "B"

            elif hidden_value == "H":
                health_bar.status_health("H")
                visible_grid[row][column] = "H"

            elif hidden_value == "J":
                health_bar.status_health("J")
                visible_grid[row][column] = "J"

            else:
                print("Nothing there!")
                visible_grid[row][column] = "X"
           
            print(f"You selected row {row + 1}, column {column + 1}")

            normal_used_moves = []

            for move in move_tracker.used_moves:
                normal_used_moves.append((move[0] + 1, move[1] + 1))

            print(f"Used moves: {normal_used_moves}")
            print()
    
    elif option == '2':
        print(" ")
        print("See ya!")
        print(" ")
    else:
        raise ValueError("Not a valid option!")
    

if __name__ == "__main__":
    main()