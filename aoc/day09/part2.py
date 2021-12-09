# Advent of Code - Day 9 - Part Two


def parse(input):
    """Simplified to return list of lists of ints"""
    return [[int(val) for val in row] for row in input]


def coordinate_generator(grid):
    """yields (row_number, column_number) coordinates within the bounds of the grid"""
    grid_width = len(grid[0])
    grid_height = len(grid)
    for row_n in range(grid_height):
        for col_n in range(grid_width):
            yield (row_n, col_n)


def neighbour_coordinates(grid, point_coords):
    """Returns list of coordinates for neighbours of the given point,
    within the bounds of the grid"""
    grid_width = len(grid[0])
    grid_height = len(grid)
    point_row, point_col = point_coords
    neighbour_coords = [
        (point_row, point_col - 1),
        (point_row, point_col + 1),
        (point_row - 1, point_col),
        (point_row + 1, point_col),
    ]
    in_grid_neighbours = [
        (row_n, col_n)
        for row_n, col_n in neighbour_coords
        if row_n >= 0 and row_n < grid_height and col_n >= 0 and col_n < grid_width
    ]
    return in_grid_neighbours


def is_minimum(grid, point):
    row, col = point
    point_val = grid[row][col]
    neighbour_vals = [
        grid[row_n][col_n] for row_n, col_n in neighbour_coordinates(grid, point)
    ]
    if all(point_val < val for val in neighbour_vals):
        return True
    else:
        return False


def score(basins, grid, top=3):
    basins.sort(key=len, reverse=True)
    top_basins = basins[:3]
    # print(f"Top basins: {top_basins}")
    score = 1
    for basin in top_basins:
        score *= len(basin)
    return score


def find_basin(grid, minimum_point):
    # BFS
    queue = {minimum_point}
    basin = set()
    while len(queue) > 0:
        check_point_coords = queue.pop()
        basin.add(check_point_coords)
        nearest_neighbour_lows = set(
            [
                (col_n, row_n)
                for col_n, row_n in neighbour_coordinates(grid, check_point_coords)
                if grid[col_n][row_n] < 9
            ]
        )
        queue |= nearest_neighbour_lows - basin
    return basin


def result(input):
    grid = parse(input)
    # find minimum points and fan out from there for basins
    mins = [point for point in coordinate_generator(grid) if is_minimum(grid, point)]
    # print(f"mins: {mins}")
    basins = [find_basin(grid, min_point) for min_point in mins]
    return score(basins, grid)


sample_input = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]

input = sample_input
# print(input)
# print(parse(input))
# print(parse_to_map(input))
# print(result(input))
