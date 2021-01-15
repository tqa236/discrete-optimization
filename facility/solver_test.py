import unittest

from solver import facility_location, parse_input


class Test(unittest.TestCase):
    def test_1(self):
        file_location = "data/fl_3_1"
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        facilities, customers = parse_input(input_data)
        solution, obj = facility_location(facilities, customers)
        self.assertEqual(obj, 2545.771137048475)


if __name__ == "__main__":
    unittest.main()
