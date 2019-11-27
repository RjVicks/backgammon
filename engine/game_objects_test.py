import game_objects as go

board = go.Board()
board.show()

yellow_player = "y"
purple_player = "p"

# Test set point
print("Test set_point")
board.set_point(yellow_player, 1, 2)
board.set_point(purple_player, 6, 5)
board.show()

# Test move
print("Test move")
board.move(yellow_player, 1, 2)
board.move(yellow_player, 1, 2)
board.show()

# Test take yellow takes purple
print("Test take: Yellow takes purple")
board = go.Board()
board.set_point(yellow_player, 1, 2)
board.set_point(purple_player, 3, 1)
board.move(yellow_player, 1, 3)
board.show()

# Test take purple takes yellow
print("Test take: Purple takes yellow")
board = go.Board()
board.set_point(purple_player, 1, 2)
board.set_point(yellow_player, 3, 1)

board.move(purple_player, 1, 3)
board.show()

# Test empty move to space
print("Test empty move to space")
board = go.Board()
board.move(purple_player, 1, 3)
board.show()
