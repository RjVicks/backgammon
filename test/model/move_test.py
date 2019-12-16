import game_objects as go
import move as mv

board = go.Board()
board.show()

yellow_player = "y"
purple_player = "p"
point_0, point_5, point_1 = 0, 5, 1
num_checkers_1, num_checkers_5 = 1, 5

# Test move to empty point
print("Test yellow moves from point 1 to empty point 1")
board.set_point(yellow_player, point_0, num_checkers_1)
board.show()
print(" After move")
mv.move(board, yellow_player, point_0, point_1)

board.show()

# Test move to players own point
print("Yellow moves from point 1 to owned point 2")
board.set_point(yellow_player, point_0, num_checkers_1)
mv.move(board, yellow_player, point_0, point_1)
board.show()

# Test yellow takes purple
print("Yellow takes purple at point 6 from point 2")
board.set_point(purple_player, point_5, num_checkers_1)
mv.move(board, yellow_player, point_1, point_5)
board.show()

# Yellow fails to move to point occupied by purple
print("Yellow fails to move to point 6 occupied by purple")
board.set_point(purple_player, point_5, num_checkers_5)
board.show()
move_status = mv.move(board, yellow_player, point_1, point_5)
print(str(move_status))
board.show()

# Purple moves from bar to opponents home
print("Purple enters from bar to opponents home")
move_status = mv.enter(board, purple_player, 23)
board.show()
