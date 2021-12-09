# Advent of Code - Day 9 - Part One


class Point:
    def __init__(self, x_coord, y_coord, val):
        self.coord_x = x_coord
        self.coord_y = y_coord
        self.val = val


def default_value():
    return 999


def parse_to_map(input):
    map = {}
    for y_coord, line in enumerate(input):
        vals = [int(val) for val in line]
        for x_coord, val in enumerate(vals):
            map[x_coord, y_coord] = Point(x_coord, y_coord, val)
    return map


def neighbour_vals(point, floor_map):
    N = floor_map.get((point.coord_x, point.coord_y - 1), 999)
    S = floor_map.get((point.coord_x, point.coord_y + 1), 999)
    E = floor_map.get((point.coord_x - 1, point.coord_y), 999)
    W = floor_map.get((point.coord_x + 1, point.coord_y), 999)
    return [point.val if isinstance(point, Point) else point for point in [N, S, E, W]]


def risk_level(height, risk=1):
    return height + risk


def result(input):
    floor_map = parse_to_map(input)
    lows = []
    for point in floor_map.values():
        if all(point.val < height for height in neighbour_vals(point, floor_map)):
            lows.append(point.val)
    return sum([risk_level(height) for height in lows])


sample_input = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]

input = sample_input
# print(input)
# print(parse_to_map(input))
print(result(input))
