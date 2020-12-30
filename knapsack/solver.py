#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import deepcopy
from collections import namedtuple

Item = namedtuple("Item", ["index", "value", "weight"])


def parse_input(input_data):
    lines = input_data.split("\n")

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))
    return items, capacity


def maximum_value(items, capacity):
    n = len(items)
    optimal = [0]
    value = [[0 for w in range(capacity + 1)] for _ in range(2)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if w == 0:
                value[i % 2][w] = 0
            elif items[i - 1].weight <= w:
                value[i % 2][w] = max(
                    items[i - 1].value + value[(i - 1) % 2][w - items[i - 1].weight],
                    value[(i - 1) % 2][w],
                )
            else:
                value[i % 2][w] = value[(i - 1) % 2][w]
        optimal.append(value[i % 2][-1])
    res = value[n % 2][-1]
    taken = [0 for _ in items]
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == optimal[i - 1]:
            continue
        taken[i - 1] = 1
        res = res - items[i - 1].value
    return value[n % 2][-1], taken


def print_output(value, taken):
    output_data = str(value) + " " + str(0) + "\n"
    output_data += " ".join(map(str, taken))
    return output_data


def solve_it(input_data):
    items, capacity = parse_input(input_data)
    value, taken = maximum_value(items, capacity)
    return print_output(value, taken)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)"
        )
