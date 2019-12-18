import game_objects as go
import turn


def set_up_board(board, yellow_player, purple_player):
    board.set_point(yellow_player, 5, 5)
    board.set_point(yellow_player, 7, 3)
    board.set_point(yellow_player, 12, 5)
    board.set_point(yellow_player, 23, 2)

    board.set_point(purple_player, 18, 5)
    board.set_point(purple_player, 16, 3)
    board.set_point(purple_player, 11, 5)
    board.set_point(purple_player, 0, 2)


def switch_active_player(active_player):
    if active_player == "y":
        return "p"
    elif active_player == "p":
        return "y"


game_incomplete = True
board = go.Board()
dice = go.Dice()
yellow_player = "y"
purple_player = "p"
active_player = yellow_player

set_up_board(board, yellow_player, purple_player)
print("\n\nStart Game.")
board.show()

while game_incomplete:
    turn.make_turn(board, active_player, dice)
    active_player = switch_active_player(active_player)
