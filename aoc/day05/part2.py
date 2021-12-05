# Advent of Code - Day 5 - Part Two

import re
from collections import defaultdict


def parse(input):
    coords = []
    for line in input:
        m = re.match(r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)", line)
        coords.append(m.groupdict())
    return coords


def intermediate_grid_points(coord_dict):
    """Takes {'x1': '6', 'y1': '4', 'x2': '2', 'y2': '0'}
    returns [(6,4),(2,0),(5,3),(4,2),(3,1)]"""
    x1 = int(coord_dict["x1"])
    x2 = int(coord_dict["x2"])
    y1 = int(coord_dict["y1"])
    y2 = int(coord_dict["y2"])
    xes, yes = None, None
    if x1 < x2:
        xes = [x for x in range(x1, x2 + 1)]
    elif x1 > x2:
        xes = [x for x in range(x1, x2 - 1, -1)]
    if y1 < y2:
        yes = [y for y in range(y1, y2 + 1)]
    elif y1 > y2:
        yes = [y for y in range(y1, y2 - 1, -1)]
    # handle vertical and horizontal where x or y needs to be repeated
    if xes is None:
        xes = [x1] * len(yes)
    if yes is None:
        yes = [y1] * len(xes)
    return list(zip(xes, yes))


def result(input):
    grid = defaultdict(int)
    coords = parse(input)
    # process horizontal lines first
    for coord in coords:
        xy_coords = intermediate_grid_points(coord)
        for point in xy_coords:
            grid[point] += 1
    return len([x for x in grid.values() if x > 1])
