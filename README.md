README
The RAMA Fishing game is a command line grid based game

| Method/function | Primary author | Techniques demonstrated |
|---|---|---|
| generate_grid | Alexander Moore | optional parameters and/or keyword arguments |
| place_fish | Alexander Moore | comprehensions or generator expressions |
| __contains__ | Aidan Collins | magic methods other than __init__ |
| validate_move | Aidan Collins | set operations |
| get_random_item | Matteo Palma | use of json.load() |
| print_health | Matteo Palma | f-strings containing expressions |






Functions: 

Matteo Palma (princemetici/mpalma04)

I created the healthbar file and status_health function which modifies the healthbar depending on your catch. If you catch a fish your health remains, if you catch a bad item like a bomb or a puffer, you lose a bar of health. If you catch a healing potion while your health is below full you will get healed.

I also created the JSON file containing all of the items that can be called from the .load() from the get_random_items function


Aidan Collins(acolli09-stack)

I created the guesses.py file and the MoveTracker system which keeps track of all the locations the player has already guessed. My code prevents repeated guesses by checking whether a grid position has already been used before allowing the player to continue.

I also created the get_player_guess function which handles player input and validates each guess. If the player enters an invalid row or column, or chooses the same spot twice, the program displays an error message and asks for a new input until a valid move is entered.


Alexander Moore (amoore28-del)

I created the ocean_builder.py file which is responsible for generating and displaying the game board. I used loops to repeatedly create rows and columns for the grid, and I used lists to store the board as a 2D structure that can be updated throughout the game.

I also used loops and random placement logic to help place fish and other hidden items in different locations on the board each time the game starts. In addition, the grid display system uses loops to print the visible game board to the screen after every turn so the player can track their progress and previous guesses while playing the game.


Note: Aidan Collins used his computer for a bulk of the project as Alex and Matteo had problems with commit and pulling the files. So Matteo fully wrote his part but some of it was written on my computer: he gave Aidan the code and Aidan pasted it, same with Alex Moore. We also all claim credit for the main_game.py as we all contributed to that equally.


Bibliography: