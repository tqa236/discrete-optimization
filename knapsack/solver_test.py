import unittest

from solver import parse_input, solve_it, maximum_value


class Test(unittest.TestCase):
    def test_1(self):
        file_location = "data/ks_4_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        items, capacity = parse_input(input_data)
        value, taken = maximum_value(items, capacity)
        self.assertEqual(value, 19)
        self.assertEqual(taken, [0, 0, 1, 1])

    def test_2(self):
        file_location = "data/ks_50_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        items, capacity = parse_input(input_data)
        value, taken = maximum_value(items, capacity)
        self.assertEqual(value, 142156)

    def test_3(self):
        file_location = "data/ks_200_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        items, capacity = parse_input(input_data)
        value, taken = maximum_value(items, capacity)
        self.assertEqual(value, 100236)


if __name__ == "__main__":
    unittest.main()
