import unittest

from solver import parse_input, graph_coloring, find_minimum_colors


class Test(unittest.TestCase):
    def test_1(self):
        file_location = "data/gc_4_1"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        node_count, edges = parse_input(input_data)
        solution, k = find_minimum_colors(node_count, edges)
        self.assertEqual(k, 2)

    def test_2(self):
        file_location = "data/gc_50_1"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        node_count, edges = parse_input(input_data)
        solution, k = find_minimum_colors(node_count, edges)
        self.assertEqual(k, 4)

    def test_3(self):
        file_location = "data/gc_100_7"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        node_count, edges = parse_input(input_data)
        solution, k = find_minimum_colors(node_count, edges)
        self.assertEqual(k, 4)


if __name__ == "__main__":
    unittest.main()
