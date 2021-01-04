import unittest

from solver import parse_input, tsp


class Test(unittest.TestCase):
    def test_1(self):
        file_location = "data/tsp_5_1"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        nodeCount, points = parse_input(input_data)
        obj, solution = tsp(nodeCount, points)
        self.assertEqual(obj, 2)


if __name__ == "__main__":
    unittest.main()
