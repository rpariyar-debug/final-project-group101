import random 

def generate_grid(rows, cols):
    """
    Create a game grid.

    Args:
        rows (int): Number of rows.
        cols (int): Number of columns.

    Returns:
        list: A 2D list representing the grid.
    """

    grid = []

    for _ in range(rows):
        row = []

        for _ in range(cols):
            row.append("~")

        grid.append(row)

    return grid

def place_fish(grid, fish_count):
    """
    Randomly places fish on empty spots in the grid.

    Args:
        grid (list): The game grid.
        fish_count (int): Number of fish to place.

    Returns:
        list: The updated grid with fish added.

    Side effects:
        Modifies the original grid by placing fish symbols.
        """
    
    rows = len(grid)
    cols = len(grid[0])
    
    placed = 0
    
    while placed < fish_count:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        if grid[row][col] == "~":
            grid[row][col] = "F"
            placed += 1
    return grid

def place_items(grid, item_symbol, item_count):
    """
    Randomly places items on empty spots in the grid.

    Args:
        grid (list): The game grid.
        item_symbol (str): Symbol used for the item.
        item_count (int): Number of items to place.

    Returns:
        list: The updated grid with items added.

    Side effects:
        Modifies the original grid by placing item symbols.
        """
    rows = len(grid)
    cols = len(grid[0])

    placed = 0

    while placed < item_count:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        if grid[row][col] == "~":
            grid[row][col] = item_symbol
            placed += 1

    return grid

def print_grid(grid):
    """
    Print the grid to the screen

    Args:
        grid (list): The game grid.

    Side effects:
        Prints the grid to the console.
    """
    
    
    print("+" + "---+" * len(grid[0]))

    for row in grid:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * len(grid[0]))



if __name__ == "__main__":
    game_grid = generate_grid(5, 5)
    print_grid(game_grid)
    place_fish(game_grid, 5)

    