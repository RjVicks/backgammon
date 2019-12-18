import random


class Point:

    def __init__(self, occupied_by, num_checkers):
        self.num_checkers = num_checkers
        self.occupied_by = occupied_by

    def get_info(self):
        return '{}{}'.format(self.occupied_by, self.num_checkers)

    def set_checkers(self, player_colour, number):
        self.num_checkers = number
        self.occupied_by = player_colour

    def increment(self, player_colour):
        self.occupied_by = player_colour
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
        self.yellow_bar = 0
        self.purple_bar = 0
        self.yellow_home = 0
        self.purple_home = 0

    def add_checker_to_home(self, player_colour):
        if player_colour == "Yellow":
            self.yellow_home += 1
        elif player_colour == "Purple":
            self.purple_home += 1

    def is_player_on_bar(self, player_colour):
        if player_colour == "Yellow":
            return self.yellow_bar >= 1
        elif player_colour == "Purple":
            return self.purple_bar >= 1

    def add_checker_to_bar(self, player_colour):
        if player_colour == "Yellow":
            self.yellow_bar += 1
        elif player_colour == "Purple":
            self.purple_bar += 1

    def remove_checker_from_bar(self, player_colour):
        if player_colour == "Yellow":
            self.yellow_bar -= 1
        elif player_colour == "Purple":
            self.purple_bar -= 1

    def add_checker(self, player_colour, index):
        self.points[index].increment(player_colour)

    def remove_checker(self, index):
        self.points[index].decrement()

    def is_point_players(self, player_colour, index):
        return self.points[index].occupied_by == player_colour

    def is_point_empty(self, index):
        return self.points[index].occupied_by == "e"

    def is_point_takeable(self, player_colour, index):
        is_opponents = not self.is_point_players(player_colour, index)
        is_isolated = self.get_num_checkers(index) == 1
        return is_opponents and is_isolated

    def get_num_checkers(self, index):
        return self.points[index].num_checkers

    def set_point(self, player_colour, index, number):
        self.points[index].set_checkers(player_colour, number)

    def show(self):
        for index in range(6):
            col_1 = str(index+1) + "|  " + self.points[index].get_info() + "\t\t"
            col_2 = str(index+7) + "|  " + self.points[index+6].get_info() + "\t\t"
            col_3 = str(index+13) + "|  " + self.points[index+12].get_info() + "\t\t"
            col_4 = str(index+19) + "|  " + self.points[index+18].get_info()
            print(col_1 + col_2 + col_3 + col_4)
        print("y bench: {} \t p bench: {}".format(self.yellow_bar, self.purple_bar))
        print("------- END --------\n")


class Dice:

    def __init__(self):
        self.values = [0, 0, 0, 0]

    def roll(self):
        self.values[0] = random.randint(1, 6)
        self.values[1] = random.randint(1, 6)
        if self.values[0] == self.values[1]:
            self.values[2] = self.values[0]
            self.values[3] = self.values[0]

    def get_available_values(self):
        available_moves = []
        for value in self.values:
            if value != 0:
                available_moves.append(value)
        return available_moves

    def remove_from_available_values(self, value):
        for index, _value in enumerate(self.values):
            if value == _value:
                self.values[index] = 0
                return

    def number_of_values_left(self):
        sum = 0
        for value in self.values:
            if value != 0:
                sum += 1

        return sum

    def show(self):
        print("Dice: {} {} {} {}".format(self.values[0], self.values[1], self.values[2], self.values[3]))
