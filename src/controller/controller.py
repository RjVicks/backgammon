def get_start_and_end_points(self):
    input_string = input("Player please make a move: ")
    positions = input_string.split(' ')
    return int(positions[0]), int(positions[1])
