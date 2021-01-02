#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from ortools.sat.python import cp_model


def parse_input(input_data):
    lines = input_data.split("\n")
    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    return node_count, edges


class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.colors = range(10)
        self.node_colors = []

    def OnSolutionCallback(self):
        for v in self.__variables:
            self.node_colors.append(self.colors[self.Value(v)])
        self.StopSearch()

    def SolutionCount(self):
        return self.node_colors


def graph_coloring(num_nodes, connections, k):
    model = cp_model.CpModel()
    nodes = [model.NewIntVar(0, k - 1, "x%i" % i) for i in range(num_nodes)]

    for conn in connections:
        model.Add(nodes[conn[0]] != nodes[conn[1]])

    solver = cp_model.CpSolver()
    solution_printer = SolutionPrinter(nodes)
    solver.SearchForAllSolutions(model, solution_printer)
    colors = solution_printer.SolutionCount()
    return colors


def print_output(node_count, solution):
    output_data = str(node_count) + " " + str(1) + "\n"
    output_data += " ".join(map(str, solution))
    return output_data


def find_minimum_colors(node_count, edges):
    k = 1
    solution = None
    while not solution and k < node_count:
        k += 1
        solution = graph_coloring(node_count, edges, k)
    return solution, k


def solve_it(input_data):
    node_count, edges = parse_input(input_data)
    solution, k = find_minimum_colors(node_count, edges)
    output_data = print_output(k, solution)
    return output_data


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)"
        )
