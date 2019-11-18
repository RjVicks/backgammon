import random


class Point:

    def __init__(self, num_checkers):
        self.num_checkers = num_checkers

    def get_info(self):
        return '{}'.format(self.num_checkers)

    def set_checkers(self, number):
        self.num_checkers = number

    def increment(self):
        self.num_checkers = self.num_checkers + 1

    def decrement(self):
        self.num_checkers = self.num_checkers - 1


class Board:

    def __init__(self):
        self.points = [Point(0) for x in range(24)]

    def set_point(self, index, number):
        self.points[index].set_checkers(number)

    def show(self):
        for index in range(6):
            col_1 = str(index) + "|  " + self.points[index].get_info() + "\t\t"
            col_2 = str(index+6) + "|  " + self.points[index+6].get_info() + "\t\t"
            col_3 = str(index+12) + "|  " + self.points[index+12].get_info() + "\t\t"
            col_4 = str(index+18) + "|  " + self.points[index+18].get_info()
            print(col_1 + col_2 + col_3 + col_4)

    def move(self, position1, position2):
        self.points[position1].decrement()
        self.points[position2].increment()


class Dice:

    def __init__(self):
        self.value = [0, 0]

    def roll(self):
        self.value[0] = random.randint(1, 6)
        self.value[1] = random.randint(1, 6)

    def show(self):
        print("Dice: {} {}".format(self.value[0], self.value[1]))


class Player:

    def __init__(self, colour, board):
        self.colour = colour
        self.dice = Dice()
        self.board = board

    def roll_dice(self):
        self.dice.roll()

    def show(self):
        self.board.show()
        self.dice.show()
