#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import sys
from collections import namedtuple

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

Point = namedtuple("Point", ["x", "y"])


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    index = routing.Start(0)
    route_distance = 0
    path = []
    while not routing.IsEnd(index):
        path.append(index)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    route_distance = route_distance / 10 ** 9
    return route_distance, path


def tsp(data):
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.seconds = 600
    solution = routing.SolveWithParameters(search_parameters)
    if solution:

        route_distance, path = print_solution(manager, routing, solution)
    return route_distance, path


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
    all_distances = []
    for point in points:
        distances = []
        for point2 in points:
            distances.append(int(length(point, point2) * 10 ** 9))
        all_distances.append(distances)
    data = {}
    data["distance_matrix"] = all_distances
    data["num_vehicles"] = 1
    data["depot"] = 0
    return data


def print_output(obj, solution):
    output_data = "%.2f" % obj + " " + str(0) + "\n"
    output_data += " ".join(map(str, solution))
    return output_data


def solve_it(input_data):
    data = parse_input(input_data)
    obj, solution = tsp(data)
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
