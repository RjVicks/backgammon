import random


class Point:

    def __init__(self, occupied_by, num_checkers):
        self.num_checkers = num_checkers
        self.occupied_by = occupied_by

    def get_info(self):
        return '{}{}'.format(self.occupied_by, self.num_checkers)

    def set_checkers(self, player, number):
        self.num_checkers = number
        self.occupied_by = player

    def increment(self, player):
        self.occupied_by = player
        self.num_checkers += 1

    def decrement(self):
        if self.num_checkers == 0:
            pass
        else:
            self.num_checkers -= 1
            if self.num_checkers == 0:
                self.occupied_by = "e"


class Board:

    def __init__(self):
        self.points = [Point("e", 0) for x in range(24)]
        self.y_bench = 0
        self.p_bench = 0

    def get_height(self, index):
        index -= 1
        return self.points[index].num_checkers

    def set_point(self, player, index, number):
        index -= 1
        self.points[index].set_checkers(player, number)

    def move(self, player_turn, start_point, end_point):
        start_point -= 1
        end_point -= 1
        is_empty = self.points[end_point].occupied_by == "e"
        is_players = self.points[end_point].occupied_by == player_turn
        if is_empty or is_players:
            self.points[start_point].decrement()
            self.points[end_point].increment(player_turn)

        if self.is_takeable(player_turn, end_point):
            self.points[end_point].decrement()
            if player_turn == "y":
                self.p_bench += 1
            elif player_turn == "p":
                self.y_bench += 1
            self.points[start_point].decrement()
            self.points[end_point].increment(player_turn)

    def is_takeable(self, player_turn, end_point):
        is_occupied_by_opponent = self.opposite_player(player_turn) == self.points[end_point].occupied_by
        is_isolated = self.points[end_point].num_checkers == 1
        if is_occupied_by_opponent and is_isolated:
            return True
        else:
            return False

    def opposite_player(self, player_turn):
        if player_turn == "y":
            return "p"
        if player_turn == "p":
            return "y"

    def show(self):
        for index in range(6):
            col_1 = str(index+1) + "|  " + self.points[index].get_info() + "\t\t"
            col_2 = str(index+7) + "|  " + self.points[index+6].get_info() + "\t\t"
            col_3 = str(index+13) + "|  " + self.points[index+12].get_info() + "\t\t"
            col_4 = str(index+19) + "|  " + self.points[index+18].get_info()
            print(col_1 + col_2 + col_3 + col_4)
        print("y bench: {} \t p bench: {}".format(self.y_bench, self.p_bench))
        print("------- END --------\n")


class Dice:

    def __init__(self):
        self.value = [0, 0]

    def roll(self):
        self.value[0] = random.randint(1, 6)
        self.value[1] = random.randint(1, 6)

    def show(self):
        print("Dice: {} {}".format(self.value[0], self.value[1]))
