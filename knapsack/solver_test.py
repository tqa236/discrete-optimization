import unittest

from solver import parse_input, solve_it, maximum_value


class Test(unittest.TestCase):
    def test_1(self):
        file_location = "data/ks_4_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        items, capacity = parse_input(input_data)
        value, taken = solve_it(items, capacity)
        value, taken = maximum_value(items, capacity)
        self.assertEqual(value, 18)
        self.assertEqual(taken, [1, 1, 0, 0])


if __name__ == "__main__":
    unittest.main()
