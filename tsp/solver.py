#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import sys
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def length(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def parse_input(input_data):
    lines = input_data.split("\n")

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount + 1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))
    return nodeCount, points


def tsp(nodeCount, points):
    solution = range(0, nodeCount)

    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount - 1):
        obj += length(points[solution[index]], points[solution[index + 1]])

    return obj, solution


def print_output(obj, solution):
    output_data = "%.2f" % obj + " " + str(0) + "\n"
    output_data += " ".join(map(str, solution))
    return output_data


def solve_it(input_data):
    nodeCount, points = parse_input(input_data)
    obj, solution = tsp(nodeCount, points)
    output_data = print_output(obj, solution)
    return output_data


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)"
        )
