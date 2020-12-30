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
        file_location = "data/ks_lecture_dp_2"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        items, capacity = parse_input(input_data)
        value, taken = maximum_value(items, capacity)
        weight = sum([items[i].weight for i, value in enumerate(taken) if value == 1])
        self.assertEqual(value, 44)
        print(weight, capacity)
        self.assertTrue(weight <= capacity)

    # def test_3(self):
    #     file_location = "data/ks_19_0"
    #     with open(file_location, "r") as input_data_file:
    #         input_data = input_data_file.read()
    #     items, capacity = parse_input(input_data)
    #     value, taken = maximum_value(items, capacity)
    #     weight = sum([items[i].weight for i, value in enumerate(taken) if value == 1])
    #     self.assertEqual(value, 12248)
    #     print(weight, capacity)
    #     self.assertTrue(weight <= capacity)

    # def test_4(self):
    #     file_location = "data/ks_50_0"
    #     with open(file_location, "r") as input_data_file:
    #         input_data = input_data_file.read()
    #     items, capacity = parse_input(input_data)
    #     value, taken = maximum_value(items, capacity)
    #     weight = sum([items[i].weight for i, value in enumerate(taken) if value == 1])
    #     self.assertEqual(value, 142156)
    #     print(weight, capacity)
    #     self.assertTrue(weight <= capacity)

    # def test_5(self):
    #     file_location = "data/ks_200_0"
    #     with open(file_location, "r") as input_data_file:
    #         input_data = input_data_file.read()
    #     items, capacity = parse_input(input_data)
    #     value, taken = maximum_value(items, capacity)
    #     self.assertEqual(value, 100236)
    #     weight = sum([items[i].weight for i, value in enumerate(taken) if value == 1])
    #     self.assertTrue(weight <= capacity)


if __name__ == "__main__":
    unittest.main()
