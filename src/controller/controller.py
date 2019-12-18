def get_start_and_end_points(active_player):
    input_string = input("Player {} please make a move: ".format(active_player))
    positions = input_string.split(' ')
    return int(positions[0]) - 1, int(positions[1]) - 1
