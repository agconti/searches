import unittest
import random
from linear_search import linear_search


class TestLinearSearch(unittest.TestCase):

    def setUp(self):
        self.items_length = 20
        self.unsorted_values = [random.random() for i in range(self.items_length)]
        self.target = random.choice(self.unsorted_values)

    def test_linear_search_returns_an_index(self):
        position = linear_search(self.unsorted_values, self.target)

        assert position in range(self.items_length)
        assert isinstance(position, int)

    def test_linear_search_raises_an_error_with_an_invalid_target(self):
        target = 1
        try:
            linear_search(self.unsorted_values, target)
        except ValueError as e:
            self.assertEqual(e.message, "{} was not found in the list".format(target))

    def test_linear_search_finds_target(self):
        position = linear_search(self.unsorted_values, self.target)
        self.assertEqual(self.unsorted_values[position], self.target)

if __name__ == '__main__':
    unittest.main()
