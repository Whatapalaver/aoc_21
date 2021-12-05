# Advent of Code - Day 5 - Part One
import re
from collections import defaultdict


def parse(input):
    horiz_coords = []
    vert_coords = []
    for line in input:
        m = re.match(r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)", line)
        if m.group("x1") == m.group("x2"):
            vert_coords.append(m.groupdict())
        elif m.group("y1") == m.group("y2"):
            horiz_coords.append(m.groupdict())
    return horiz_coords, vert_coords


def intermediate_grid_points(first, second):
    first = int(first)
    second = int(second)
    if first < second:
        initial, final = first, second
    else:
        initial, final = second, first
    return [x for x in range(initial, final + 1)]


def result(input):
    grid = defaultdict(int)
    horiz_coords, vert_coords = parse(input)
    # process horizontal lines first
    for coord in horiz_coords:
        x_coords = intermediate_grid_points(coord["x1"], coord["x2"])
        for x in x_coords:
            grid[(str(x), coord["y1"])] += 1
    # process vertical lines
    for coord in vert_coords:
        y_coords = intermediate_grid_points(coord["y1"], coord["y2"])
        for y in y_coords:
            grid[coord["x1"], str(y)] += 1
    return len([x for x in grid.values() if x > 1])
