import game_objects as go
import unittest


class TestGameObjects(unittest.TestCase):

    def setUp(self):
        self.yellow_player = "Yellow"
        self.purple_player = "Purple"
        self.board = go.Board()
        self.points = [1, 6]
        self.num_checkers = [1, 5]
        self.board.set_point(self.yellow_player, self.points[0], self.num_checkers[0])

    def test_set_point(self):
        self.assertEqual(self.board.get_num_checkers(self.points[0]), 1)

    def test_is_point_empty(self):
        self.assertTrue(self.board.is_point_empty(self.points[1]))

    def test_is_point_players(self):
        self.assertTrue(self.board.is_point_players(self.yellow_player, self.points[0]))
        self.assertFalse(self.board.is_point_players(self.purple_player, self.points[0]))
        self.assertFalse(self.board.is_point_players(self.yellow_player, self.points[1]))

    def test_is_point_takeable(self):
        self.assertTrue(self.board.is_point_takeable(self.purple_player, self.points[0]))
        self.assertFalse(self.board.is_point_takeable(self.purple_player, self.points[1]))


if __name__ == '__main__':
    unittest.main()
