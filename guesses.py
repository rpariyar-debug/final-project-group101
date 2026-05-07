class MoveTracker: 
    def __init__(self, rows=7, columns=7):
        self.rows = rows
        self.columns = columns
        self.used_moves = set()
    
    def __contains__(self, move):
        return move in self.used_moves
    
    def is_in_bounds(self, row, column):
        return 0 <= row < self.rows and 0 <= column < self.columns
    
    def validate_move(self, row, column):
        move = (row, column)
        if not self.is_in_bounds(row, column):
            print("That spot is outside the ocean grid, Choose a row and column from 1 to 7.")
            return False
        if move in self.used_moves:
            print("You already fished in that spot. Choose a new location.")
            return False
        
        return True
    
    def add_move(self, row, column):
        self.used_moves.add((row, column))
    
    def guesses_left(self, max_guesses):
        return max_guesses - len(self.used_moves)
    
def get_player_guess(move_tracker):
    while True:
        try:
            row = int(input("Choose a row from 1 to 7: ")) - 1
            column = int(input("Choose a column from 1 to 7: ")) - 1
            
            if move_tracker.validate_move(row, column):
                move_tracker.add_move(row, column)
                return row, column
        except ValueError:
            print("Please enter numbers only.")

