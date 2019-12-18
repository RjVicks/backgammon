import game_objects as go
import move as mv
import unittest


class TestMove(unittest.TestCase):

    def setUp(self):
        self.yellow_player = "y"
        self.purple_player = "p"
        self.board = go.Board()
        self.points = [0, 1, 5]
        self.num_checkers = [1, 5]
        self.board.set_point(self.yellow_player, self.points[0], self.num_checkers[0])

    def test_move_to_empty(self):
        mv.move(self.board, self.yellow_player, self.points[0], self.points[1])
        self.assertEqual(self.board.get_num_checkers(self.points[1]), 1)
        self.assertEqual(self.board.get_num_checkers(self.points[0]), 0)

    def test_move_to_players_own_point(self):
        self.board.set_point(self.yellow_player, self.points[1], self.num_checkers[0])
        mv.move(self.board, self.yellow_player, self.points[0], self.points[1])
        self.assertEqual(self.board.get_num_checkers(self.points[1]), 2)

    def test_yellow_takes_purple(self):
        self.board.set_point(self.purple_player, self.points[1], self.num_checkers[0])
        mv.move(self.board, self.yellow_player, self.points[0], self.points[1])
        self.assertEqual(self.board.get_num_checkers(self.points[1]), 1)
        self.assertTrue(self.board.is_point_players(self.yellow_player, self.points[1]))
        self.assertTrue(self.board.is_player_on_bar(self.purple_player))

    # Purple enters from bar
    def test_purple_enters_from_bar(self):
        self.board.add_checker_to_bar(self.purple_player)
        mv.enter(self.board, self.purple_player, 23)
        self.assertTrue(self.board.get_num_checkers(23), 1)
        self.assertFalse(self.board.is_player_on_bar(self.purple_player))


if __name__ == '__main__':
    unittest.main()
