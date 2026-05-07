from guesses import MoveTracker, get_player_guess

tracker = MoveTracker(rows=7, columns=7)

row, column = get_player_guess(tracker)