import unittest
import random
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.items_length = 20
        self.sorted_values = [i for i in range(self.items_length)]
        self.target = random.choice(self.sorted_values)

    def test_binary_search_returns_an_index(self):
        position = binary_search(self.sorted_values, self.target)

        assert position in range(self.items_length)
        assert isinstance(position, int)

    def test_binary_search_raises_an_error_with_an_invalid_target(self):
        target = 1
        try:
            binary_search(self.sorted_values, target)
        except ValueError as e:
            self.assertEqual(e.message, "{} was not found in the list".format(target))

    def test_binary_search_finds_target(self):
        position = binary_search(self.sorted_values, self.target)
        self.assertEqual(self.sorted_values[position], self.target)

if __name__ == '__main__':
    unittest.main()
