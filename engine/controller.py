import game_objects as obj


def parse_input(input_string):
    positions = input_string.split(' ')
    return int(positions[0]), int(positions[1])


def make_turn(player):
    player.roll_dice()
    player.show()

    turn_incomplete = True
    num_complete_moves = 0

    while turn_incomplete:
        input_string = input("{} Player please make a move: ".format(player.colour))

        position_1, position_2 = parse_input(input_string)

        position_difference = abs(position_1 - position_2)
        legal_move = position_difference in (player.dice.value[0], player.dice.value[1])

        if legal_move:
            player.board.move(position_1, position_2)
            num_complete_moves = num_complete_moves + 1
        else:
            print("please make a legal move")

        turn_incomplete = num_complete_moves != 2
    print("End turn " + "--" * 24 + "\n")


def switch_player_turn(player_turn):
    if player_turn == "White":
        return "Black"
    else:
        return "White"


# Start state
board = obj.Board()
white_player = obj.Player("White", board)
black_player = obj.Player("Black", board)
playing = True
player_turn = "White"
print("Welcome to Backgammon\n")

while playing:
    if player_turn == "White":
        make_turn(white_player)
    else:
        make_turn(black_player)
    player_turn = switch_player_turn(player_turn)
    print("DEBUG: Player turn is " + player_turn)
