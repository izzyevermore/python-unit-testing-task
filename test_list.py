import unittest
from main import max_numbers
from main import descending_sort


class TestMaxNumbers(unittest.TestCase):
    def test_max_numbers(self):
        assert max_numbers([3, 5, 6, 9, 12, 78]) == 78, "The max number in [3, 5, 6, 9, 12, 78] list should be 78"

    def test_descending_sorter(self):
        assert descending_sort([10, 6, 5, 18]) == [18, 10, 6, 5], "The order in [10, 6, 5, 18] shpould be [5, 6, 10, 18]"


