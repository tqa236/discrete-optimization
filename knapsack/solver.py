#!/usr/bin/python
# -*- coding: utf-8 -*-

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


def maximum_value(items, capacity, taken, item=None):
    """Fill the knapsack with the highest values item."""
    if capacity < 0:
        taken[item.index] = 0
        return -item.value
    if not items or capacity == 0:
        return 0, []
    leave_item_value = maximum_value(capacity, items[1:])
    take_item_value = (
        maximum_value(capacity - items[0].weight, items[1:], items[0]) + items[0].value
    )
    if leave_item_value >= take_item_value:
        taken[item.index] = 0
        max_value = leave_item_value
    else:
        taken[item.index] = 1
        max_value = take_item_value
    return max_value, taken


def solve_it(items, capacity):
    """Naive solution for knapsack problem."""
    value = 0
    weight = 0
    taken = [0] * len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    return value, taken


def print_output(value, taken):
    output_data = str(value) + " " + str(0) + "\n"
    output_data += " ".join(map(str, taken))
    return output_data


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        items, capacity = parse_input(input_data)
        value, taken = solve_it(items, capacity)
        print(print_output(value, taken))
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)"
        )
