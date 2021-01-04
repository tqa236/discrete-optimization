import unittest

from solver import find_minimum_colors, graph_coloring, parse_input


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
        file_location = "data/gc_100_5"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        node_count, edges = parse_input(input_data)
        solution, k = find_minimum_colors(node_count, edges)
        self.assertEqual(k, 17)

    def test_4(self):
        file_location = "data/gc_1000_5"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        node_count, edges = parse_input(input_data)
        solution, k = find_minimum_colors(node_count, edges)
        self.assertEqual(k, 10)


if __name__ == "__main__":
    unittest.main()
