import move as mv


def make_move(board, player_colour, start_point, end_point):
    is_player_on_bar = board.is_player_on_bar(player_colour)
    if is_player_on_bar:
        return mv.enter(board, player_colour, end_point)

    _is_player_home = is_player_home(board, player_colour)
    if _is_player_home:
        if end_point == -1:
            return mv.bear_off(board, start_point)
        else:
            return mv.move(board, player_colour, start_point, end_point)

    is_standard = not is_player_on_bar and not _is_player_home
    if is_standard:
        return mv.move(board, player_colour, start_point, end_point)


def is_player_home(board, player_colour):
    sum = 0
    if player_colour == "Yellow":
        for point_index in range(6):
            if board.is_point_players(player_colour, point_index):
                sum += board.get_num_checkers(point_index)
    elif player_colour == "Purple":
        for point_index in range(18, 24):
            if board.is_point_players(player_colour, point_index):
                sum += board.get_num_checkers(point_index)
    return sum == 15
