import game_objects as go

board = go.Board()
board.show()

yellow_player = "y"
purple_player = "p"

# Test set point
print("Test set_point")
point_1, point_2 = 1, 6
num_checkers_1, num_checkers_2 = 1, 5
board.set_point(yellow_player, point_1, num_checkers_1)
board.set_point(purple_player, point_2, num_checkers_2)
board.show()

print("Is point_1 empty? : {}".format(board.is_point_empty(point_1)))  # exp False
print("Is point_1 yellow? : {}".format(board.is_point_players(yellow_player, point_1)))  # exp True
print("is point_1 takeable? : {}".format(board.is_point_takeable(purple_player, point_1)))  # exp True
