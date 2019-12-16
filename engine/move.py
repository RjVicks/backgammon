def move(self, board, player_colour, start_point, end_point):
    is_free_move = board.is_point_empty(player_colour, end_point) or board.is_point_players(player_colour, end_point)
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


def opposite_player(self, player_colour):
    if player_colour == "yellow":
        return "purple"
    elif player_colour == "purple":
        return "yellow"
