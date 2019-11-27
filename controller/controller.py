import game as gm


class Controller:

    def __init__(self):
        self.game = gm.Game()
        self.game.place((1, 1))
        self.game.place((2, 1))
        self.player_turn = "Yellow"

    def handle_input(self):
        input_string = input("Player please make a move: ")
        positions = input_string.split(' ')
        return int(positions[0]), int(positions[1])

    def get_move_positions(self):
        point_1, point_2 = self.handle_input()
        height_1 = self.game.board.get_height(point_1)
        height_2 = self.game.board.get_height(point_2) + 1
        start_position = (point_1, height_1)
        end_position = (point_2, height_2)
        return start_position, end_position

    def make_turn(self):
        self.game.yellow_player.roll_dice()
        self.game.show()

        turn_incomplete = True
        num_complete_moves = 0

        while turn_incomplete:

            start_position, end_position = self.get_move_positions()
            position_difference = abs(start_position[0] - end_position[0])

            legal_move = position_difference in (
                self.game.yellow_player.dice.value[0], self.game.yellow_player.dice.value[1])

            if legal_move:
                self.game.move(start_position, end_position)
                num_complete_moves += 1

            else:
                print("please make a legal move")

            turn_incomplete = num_complete_moves != 2
        print("--End Turn --")
