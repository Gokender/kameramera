import unittest

from kameramera import utils

class Utils(unittest.TestCase):

    def test_closest_value(self):
        value = 2
        values = [1, 5, 10]
        self.assertEqual(utils.get_closest_value(values, value), 1)