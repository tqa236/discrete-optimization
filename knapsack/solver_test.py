import unittest

from solver import (knapsack_solver, maximum_value, parse_input,
                    parse_or_tools_input)


class Test(unittest.TestCase):
    def test_homemade(self):
        file_location = "data/ks_4_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        items, capacity = parse_input(input_data)
        value, taken = maximum_value(items, capacity)
        self.assertEqual(value, 19)
        self.assertEqual(taken, [0, 0, 1, 1])

    def test_1(self):
        file_location = "data/ks_4_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        values, weights, capacities = parse_or_tools_input(input_data)
        value, taken = knapsack_solver(values, weights, capacities)
        self.assertEqual(value, 19)
        self.assertEqual(taken, [0, 0, 1, 1])

    def test_2(self):
        file_location = "data/ks_lecture_dp_2"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        values, weights, capacities = parse_or_tools_input(input_data)
        value, taken = knapsack_solver(values, weights, capacities)
        weight = sum(weights[0][i] for i, value in enumerate(taken) if value == 1)
        self.assertEqual(value, 44)
        self.assertTrue(weight <= capacities[0])

    def test_3(self):
        file_location = "data/ks_19_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        values, weights, capacities = parse_or_tools_input(input_data)
        value, taken = knapsack_solver(values, weights, capacities)
        weight = sum(weights[0][i] for i, value in enumerate(taken) if value == 1)
        self.assertEqual(value, 12248)
        self.assertTrue(weight <= capacities[0])

    def test_4(self):
        file_location = "data/ks_50_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        values, weights, capacities = parse_or_tools_input(input_data)
        value, taken = knapsack_solver(values, weights, capacities)
        weight = sum(weights[0][i] for i, value in enumerate(taken) if value == 1)
        self.assertEqual(value, 142156)
        self.assertTrue(weight <= capacities[0])

    def test_5(self):
        file_location = "data/ks_200_0"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        values, weights, capacities = parse_or_tools_input(input_data)
        value, taken = knapsack_solver(values, weights, capacities)
        weight = sum(weights[0][i] for i, value in enumerate(taken) if value == 1)
        self.assertEqual(value, 100236)
        self.assertTrue(weight <= capacities[0])


if __name__ == "__main__":
    unittest.main()
