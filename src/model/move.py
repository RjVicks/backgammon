# Responsible for move functionallity


def move(board, player_colour, start_point, end_point):
    is_free_move = board.is_point_empty(end_point) or board.is_point_players(player_colour, end_point)
    if is_free_move:
        board.remove_checker(start_point)
        board.add_checker(player_colour, end_point)
        return True

    is_takeable = board.is_point_takeable(player_colour, end_point)
    if is_takeable:
        board.remove_checker(end_point)
        board.add_checker_to_bar(opposite_player(player_colour))
        board.remove_checker(start_point)
        board.add_checker(player_colour, end_point)
        return True

    if not is_free_move and not is_takeable:
        return False


def enter(board, player_colour, end_point):
    is_free_move = board.is_point_empty(end_point) or board.is_point_players(player_colour, end_point)
    if is_free_move:
        board.remove_checker_from_bar(player_colour)
        board.add_checker(player_colour, end_point)
        return True

    is_takeable = board.is_point_takeable(player_colour, end_point)
    if is_takeable:
        board.remove_checker(end_point)
        board.add_checker_to_bar(opposite_player(player_colour))
        board.remove_checker_from_bar(player_colour)
        board.add_checker(player_colour, end_point)
        return True

    if not is_free_move and not is_takeable:
        return False


def bear_off(board, player_colour, point):
    board.remove_checker(point)


def opposite_player(player_colour):
    if player_colour == "y":
        return "p"
    elif player_colour == "p":
        return "y"
