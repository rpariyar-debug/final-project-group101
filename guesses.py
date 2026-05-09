""" Aidan is the author of this file"""
class MoveTracker: 
    """
    Keeps track of the moves the player has already guessed.
    Helps stop the player from choosing same spot twice
    """
    
    def __init__(self, rows=7, columns=7):
        """
        Sets up the move tracker with the size of the grid
        
        Args:
            rows (int): Number of rows in the grid.
            columns (int): Number of columns in the grid

        Side effects:
            Creates the used_moves set and stores the grid size
            
        Primary author: Aidan Collins
        Technique claimed: optional parameters
        """
        
        self.rows = rows
        self.columns = columns
        self.used_moves = set()
    
    def __contains__(self, move):
        """
        Checks if a move is already inside used_moves
        Args:
            move (tuple): A tuple containing the row and column.

        Returns:
            bool: True if the move was already used, otherwise False

        Side effects:
            None
        
        Primary aithor: Aidan Collins
        Technique claimed: magic methods other than __init__
        """
        
        return move in self.used_moves
    
    def is_in_bounds(self, row, column):
        """
        Checks if the row and column are actually inside grid
        Args:
            row (int): The row chosen by the player.
            column (int): The column chosen by the player

        Returns:
            bool: True if the move is inside the grid, otherwise False.

        Side effects:
            None
        
        Primary author: Aidan Collins
        """
        
        return 0 <= row < self.rows and 0 <= column < self.columns
    
    def validate_move(self, row, column):
        """
        Checks if a move is allowed before adding it to game
        Args:
            row (int): The row chosen by the player.
            column (int): The column chosen by the player

        Returns:
            bool: True if the move is valid, otherwise False

        Side effects:
            Prints error messages if the move is invalid
        
        Primary author: Aidan Collins
        """
        
        move = (row, column)
        if not self.is_in_bounds(row, column):
            print("That spot is outside the ocean grid, Choose a row and column from 1 to 7.")
            return False
        if move in self.used_moves:
            print("You already fished in that spot. Choose a new location.")
            return False
        
        return True
    
    def add_move(self, row, column):
        """
        adds valid move to the set of moves already guessed
        Args:
            row (int): The row chosen by the player
            column (int): The column chosen by the player

        Side effects:
            Adds a tuple containing the row and column to used_moves
        
        Primary author: Aidan Collins
       
        """
        
        self.used_moves.add((row, column))
    
    def guesses_left(self, max_guesses):
        """
         Finds how many guesses the player has left
         Args:
            max_guesses (int): Maximum number of guesses allowed

        Returns:
            int: Number of guesses remaining

        Side effects:
            None.
        
        Primary author: Aidan Collins
        """
        
        return max_guesses - len(self.used_moves)
    
def get_player_guess(move_tracker):
    """
    Asks the player for a row and column until they enter valid guess
    Args:
        move_tracker (MoveTracker): The tracker object that stores used moves

    Returns:
        tuple: The validated row and column chosen by the player

    Side effects:
        Takes user input, prints messages, and adds valid moves to used_moves
    
    Primary author: Aidan Collins
    """
    
    while True:
        try:
            row = int(input("Choose a row from 1 to 7: ")) - 1
            column = int(input("Choose a column from 1 to 7: ")) - 1
            
            if move_tracker.validate_move(row, column):
                move_tracker.add_move(row, column)
                return row, column
        except ValueError:
            print("Please enter numbers only.")

