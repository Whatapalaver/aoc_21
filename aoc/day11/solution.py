# Advent of Code - Day 11
import os
import time
from collections import defaultdict

# Part 1 - model 100 steps
# Each step:
# -> energy += 1
# -> if energy > 9, energy drops to zero, all neighbours energy +=1
# can only flash once per step


def parse_to_grid(input):
    # Mark out of bounds with a value of 999
    grid = defaultdict(lambda: 999)
    for y_coord, line in enumerate(input):
        vals = [int(val) for val in line]
        for x_coord, val in enumerate(vals):
            grid[x_coord, y_coord] = val
    return grid


def coordinate_val_generator(grid, out_of_bound=999):
    """yields tuple of ((x_coord, y_coord), val) within the bounds of the grid"""
    for coord in grid.items():
        if coord[1] != 999:
            yield coord


def in_grid(grid, position):
    return grid[position] != 999


def neighbour_coordinate_generator(grid, point_coords):
    """Yields coordinates for neighbours of the given point,
    within the bounds of the grid"""
    x_coord, y_coord = point_coords

    neighbours = [
        (x_coord, y_coord + 1),
        (x_coord, y_coord - 1),
        (x_coord + 1, y_coord),
        (x_coord - 1, y_coord),
        (x_coord - 1, y_coord + 1),
        (x_coord - 1, y_coord - 1),
        (x_coord + 1, y_coord + 1),
        (x_coord + 1, y_coord - 1),
    ]
    for coord in neighbours:
        if in_grid(grid, coord):
            yield coord


def increment_grid(grid):
    """Increment all octopi within bounds of the grid"""
    for octor_coord, _ in coordinate_val_generator(grid):
        grid[octor_coord] += 1


def flash(grid):
    seen = set()
    flash_positions = [
        coord for coord, val in coordinate_val_generator(grid) if val > 9
    ]
    while len(flash_positions):
        position = flash_positions.pop()
        seen.add(position)
        for neighbour in neighbour_coordinate_generator(grid, position):
            grid[neighbour] += 1
            if (
                neighbour not in seen
                and neighbour not in flash_positions
                and grid[neighbour] > 9
            ):
                # prepare to test neighbours neighbours
                flash_positions.append(neighbour)

    return flash_positions


def set_zeroes(grid):
    """Set all flashed octopi (val > 9) and within bounds of the grid to zero"""
    for octor_coord, octo_val in coordinate_val_generator(grid):
        if octo_val > 9:
            grid[octor_coord] = 0


def step_actions(grid):
    increment_grid(grid)
    flash(grid)
    set_zeroes(grid)
    display_grid(grid)
    time.sleep(0.1)
    return len([val for _, val in grid.items() if val == 0])


def display_grid(grid):
    os.system("cls||echo -e \\\\033c")
    vals = [val for _, val in grid.items() if val != 999]
    i = 0
    while i < 100:
        print(vals[i : i + 10])
        i += 10


def result_part1(input):
    grid = parse_to_grid(input)
    return sum(step_actions(grid) for _ in range(100))


def result_part2(input):
    grid = parse_to_grid(input)
    step = 0
    while True:
        step += 1
        print(f"Step: {step}")
        if step_actions(grid) == 100:
            return step


sample_input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]

# sample_input = ["11111", "19991", "19191", "19991", "11111"]

input = sample_input
# print(input)
# print(result_part1(input))
print(result_part2(input))
