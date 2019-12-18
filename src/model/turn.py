import controller as user_input
import move_controller as mv


def make_turn(board, player_colour, dice):
    print("{} it is your turn".format(player_colour))
    dice.roll()
    board.show()
    dice.show()

    turn_incomplete = True

    while turn_incomplete:

        start_point, end_point = user_input.get_start_and_end_points()
        position_difference = abs(start_point - end_point)

        legal_move_difference = position_difference in dice.get_available_values()
        move_successful = mv.make_move(board, player_colour, start_point, end_point)

        if legal_move_difference and move_successful:
            dice.remove_from_available_values(position_difference)
            print("Move success")

        else:
            print("please make a legal move")

        turn_incomplete = dice.number_of_values_left() == 0
    print("--End Turn --")
