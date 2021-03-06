# Advent of Code - Day 20
from collections import defaultdict
from itertools import product


def parse_image_grid(input):
    image = defaultdict(int)
    y = 0
    for row in input[2:]:
        for x, char in enumerate(row):
            image[(x, y)] = int(char == "#")
        y += 1
    return image


def parse_image_enhancement_algo(input):
    return [int(char == "#") for char in input[0]]


def parse(input):
    algo = parse_image_enhancement_algo(input)
    initial_image = parse_image_grid(input)
    return algo, initial_image


def gen_light_image_dict(image):
    """generates default_dict with dark (1) as default but light only initialised"""
    return defaultdict(
        lambda: 0,
        {coord: val for coord, val in image.items() if val == 1},
    )


def algo_index(coord, image_dict):
    """Takes coord from image pixel and generates binary code from 3x3 grid"""
    x, y = coord
    neighbour_coords = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    bin_rep_array = [str(image_dict[nc]) for nc in neighbour_coords]
    return int("".join(bin_rep_array), 2)


def gen_image_range(boundary_min, boundary_max, pad=1):
    """Takes existing image and finds coord bounds with padding to deal with alternating lights"""
    square_range = range(boundary_min - pad, boundary_max + pad)

    return list(product(square_range, square_range))


def result_part1(input, step=2):
    algo, initial_image = parse(input)
    image_dict = initial_image
    boundary_min, boundary_max = 0, len(input[2])
    for n in range(step):
        new_image_dict = defaultdict(
            lambda: 1 if n % 2 == 1 and algo[0] == 1 else 0, image_dict
        )
        # print(f"Step: {n} {len(image_dict)}")
        new_image_matrix = gen_image_range(boundary_min, boundary_max, pad=1)
        for coord in new_image_matrix:
            index = algo_index(coord, image_dict)
            if algo[index] == 1:
                new_image_dict[coord] = 1
            else:
                new_image_dict[coord] = 0
        image_dict = new_image_dict
        boundary_min -= 1
        boundary_max += 1

    return len(gen_light_image_dict(image_dict))


def result_part2(input, step=50):
    return result_part1(input, step)


sample_input = [
    "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
    "",
    "#..#.",
    "#....",
    "##..#",
    "..#..",
    "..###",
]

actual_input = [
    "####...###.###.##.##.##..###..##.#.##.#...####..##...#..#..#....#..#..##.##..#.#.####.######.#..#.##..##....#.####.##...#.#..#.####.#.#.#..###.##..#.#.#.#...#.....###.#.#...#..#....#######....#..#...###.##.........#.#.##.#........##...#..##.......####.#.#.#.#.#.####..#..........#.##......##......###.#..##.#.#.....###.#..#...###.##........#..#.##.#.###.#..#####..##..#..#.#.#...###..##..#.###.##...#.##.#.....#.#..........#..##.#########.#.#..##.#.##..######.....####...###..###.#..##########.#.#.....###.##.##.",
    "",
    "#.#...#..##..########...##....#.#.###.#.##.##...#..###.#.##.#.#..#..##..###....#..##.##....#...##.#.",
    ".###.#..#.#.#..##.##.#.####..##.#...#.###...#.#....#.#.###..#.#..###...##..######..#..#..#####......",
    "##.#.###.#.#..###...##..###.#.#..#....#...#..#.....##..###.###.######.####.#.#...##.#.##.####..#.##.",
    "...#..##...########.##..#..#...#...#...##.#..#.#..#.##..##.#..#...#.##........#.#.#.######..#..#.#..",
    ".....###....#.##....####..#.#.#.###.###.##.#.#.###..#..##.#...##.###..#.##..##.##..#.#....####..#.#.",
    "..####..###.#..###.#.....#..#..#....#########.####.#..#.##.##..#....#.....#.#.#..#.#..#..###.##...##",
    "###.#..#####...####.##...####...#.#####.##...##.####.###...###...##...#..#.#.######.##....#....##..#",
    "...#...#.#.###..#.#..#.#.####..####.#..#...#...#.#...#...#.....##..#.....#.#.#....#####.##..#.#..###",
    "##...##..###..#..#...#..#..#.####...#.##.###.#.#....#..##....#.....#.##.###.###.#.....#####.#...#...",
    ".##.#..#..#..#.##.#.##.###.###....##.#.#...#####.#..##..#....###..#.#...##.###.#..#.####..##..######",
    "#.#..####.###.#####.###.##....##..####.##.##.#########.........#.#.....####.##.....#.#...##.#....##.",
    ".#..#.#.#..#.#.#.#.#..###....##.#.##.#....#.##.#....#####.#..###...##......#..#.#.##..##..######..##",
    "..##.####.##.....#.#######..##.##...##.####.####.##...####..#.###....#..###..##..#.####....###..##..",
    "#.#....#...#.#.#..#.#..#...#####..#.#..###.#.##...#####.....##.#....#.#.##.#..#.#..###...#.#.#..#..#",
    "##.#.#..#.###.###.##.####....###.#.##.#.#.##...###.##.#.#...##.#.##..#.##.##.#.#....#.....#.#.###...",
    ".#.##.#....#.#.#.###.##..#######.###..#...#...#####.###.#.#.###..###...###.######.#.#....#...#####.#",
    "####..#..####.#......####..##...####...##.#.######.###.###.#.#.#.#....##.#######....##.#..####..##.#",
    "..##.#..###...##....##.###.#.#.#....#..##..###..##..##..#.####..#....#.#.####..#..##.#..#....#..##.#",
    ".#..#.#..##.###....#...####...##.##..#.#..##.##.##.###....##...##.....#.###......###..#.#..###....#.",
    "###.#...#.##...####.#.##.###..#.....##.#.#...#.#..###.##..###.#..#.#.#.#.#####.#.####.##..####..##..",
    ".....#.#..#.##...#..#.....#.###.##########.##.....#..####.##.##.###.##..#.##..#....#.#..##...###.#..",
    "#..#.##.#.#.#..#....##########.###..#.#...#.##...#####..#..##..#..####.......###..#..#.###..###.##.#",
    "###.#..##..##..####...#.####..##.######....#..#...#..##...#####.####.##.####...######..#..##...##..#",
    "..##.#####...#.##..###...###.#......#.#.######.#...####.####.##.##....##..##.#.#..####.#####.######.",
    "..##..#.#..###..#.....####..#.####.##.#.####.##.....####..##..#...###.#...###...#.#.#........##...#.",
    ".#.###.##.##.#.##.##..#.#.###...##..#..#..#.##.#.#..##.#.#.#.##....##....#.#......#....#..#....##.#.",
    "#####.#.###...###.#..#.##.###...###.##.##........#.###.#...##.###.#...###.##.##..#.##.###..####.###.",
    "#....####.#..#.###....##.#.##..##.....#..#...#...##.#..#.#...#..##.#..##..######.##..####.##...#.#..",
    "..#.#..#..##.##...##.###...#...###..#.##..#.#####..#.#.##.#######.##.#.#..##..####.....#####..#.#.##",
    "#.#.....#.#.##.##.##.##......#...##.##.###..#...#.#........##....#.#.....#.##.###....#..###..#..#.##",
    "..#.#.####..#.##...#.###.##....#.##.#########.###...##...##.#.#....#...#...##.....###.##.........#..",
    "###.##.#.#...#...##...##...##.##.#..#.#....##.#.##..#..##.#.##.##..#.#.####.###.#.##.##....#.###.##.",
    "###..#.######.#.###.##.###..##.#..######..###.....###......#.##..##..#.....##..##.##..#.#....##.##.#",
    "..##.#....#.........##.##.#.#..####..##.#......#....#...##.#####..##........##....#.###...###.###..#",
    "##...###.#.#..#.#..##.#.##.####....###....##.#####.##....#.##...##..#.....#....#...######..#.#...###",
    ".##.##.#..###.#.###.#.#.###...####.##.#.#.#.####.#...####.##..###.#...##..##.####..###.#.#..##..##..",
    "#..#...#####.##...#...##..###.#.#....#.#...#########..##.....##.#.#...###......#.##.########..#.##..",
    "##..##.##.......##..##........###.#....#.####.#..#.#.###....#.#.#.#.###.#.#..##..##...##.#.....#....",
    "....#..##...#####...##..#.###....##.##..##.#....#....#..#.#...#.#####...#..##.#.##...#.#...####...##",
    "..##..####.##....#.###.####...###.#.##.##...#..##..#.###.###.#.#.######.#..#####......##..#.###.#.#.",
    "#..#.#....#...###.#.#....##.###..#....##..####.#..#.#####.#.###.######...#..###.##..####.#...##.#..#",
    "..#.##.##.#.##........#..##.....#.#.#.#.##.##..#..##...#.##...#...#.##.###..###.....##..#....#.#..##",
    "###.##...##.#.#...##...####.###.#...####..###...#.##.#..#.#.###......#.#...###..#.####.##.#.#.####..",
    "#.#.##.##...#..##..#....#.##..##......###..###...####..##...###.#.##.##..##...####.#.....#.##.##...#",
    ".....#...#.##.#..#.##.#.####.#######......##.#..#...##..#...#.###.###.#.##.#.##..#.##.##.#..#.###..#",
    "####...#####..##....##.#####...#...#...##.....##..###..#...###..#...#...##.###..###.#####...##.#....",
    "#..###...###....#.#.#.######.###..####..#####...###..###..###....##.#.##..#.##..##..#.###.#####.....",
    "#.#.##.#.####..#####.###.#..#####.#..#.#.#..#.##....##.#.#.#.#.###.###..###...#####.#.##.#.#.#..#...",
    ".#.#...#..#.##.#..####..###.#..#.########.####......#...##..#####..#...#.#..###..#.#....####....#..#",
    "##.###.###..#..##.#..#...#..####..#.###..##....#.#...######.##....##...#....#.........####.#.###.#..",
    ".##..####.##.#.#..####...#.##..##.##..###...#.....##...#......#....##...#####..#####.#.#.#...#..##..",
    ".#...##.#.###.#.#.##....###..###.##.#.##.....###.####.......#.#.#.#....##.#..#..#..#####..#....#.#.#",
    "..#.##.###.###.................###.#...#...#.##.#.###..###..#..##..#.#..###..##.#.##.#.##.##.##.#...",
    "###.#...#..#...###.......###.#.#..#####.####.#..#...##...#####..#........###.#..#.#######..####.#.##",
    "...#.##.#####.#...##.###...##.#..#..##.##.##..#.#.#.#.###...#.##..#.##.##.#.#.##...##.###....#..#.##",
    "##.#.####.##.#..#####.#.#...######.###.#.#.##.##...##.#.##.#..#...##.##.#..#...#..#..#..#..#.##.#...",
    "#.#######.#..#.##..#..#.#..#..####....#.#..#..#...#.....####...#..#.......#..#...##..##.##.##..#.#..",
    "..##.#.####.#.#.#......########..#..#.....###.#.####.#..#####.##..####.#.###....##.#.#..#.##..#####.",
    ".##.#.##.#.#..#.#.#.#...#########...#####..#...###.#.##..##.#..##...###.##.#.#.#.#...####.#.#.####.#",
    ".#####.####..##.##....#.#.#...######.#.#..#.#.#....#.#....##.#..#.###..#..#.####...###..##.#.#.#.#..",
    ".##..#..###.######.#.#.#..######.##..#..#.######....###.##..#####.....####.#.#.#...##.###.#...##.##.",
    ".#.####..##.#..#.#..#.###.##.#....##..#.#..#####.##.##...#..####..###..#........#.##..##.####...###.",
    "..##..###.#.###.#...##.#.##.##.#######..##.#....#.####.#...####...####.###.##.##...##.#..#.#....#..#",
    ".##..#.######..#.#.##.....######.#####......###.#....###.##.#.###.#..#.#.###.#.####...####.##.....##",
    ".####....#.##.##.#.#....#.##.#..#...##.....#..##......#..#######..#.##.###.#..#.###.####..###.#.#..#",
    "..#.##.#.#..##..####....#######.##...#.##.....#.#.##....#.###.#.#..#.###.#.....#.####.#.....##.#...#",
    "##...#.##..##.#.........#..#..#######.##.#..###.#.###..#.##.#..#...#..#..#.##.##.#..###.###...##.##.",
    "...#.#..###..#.##.#####.#.##...#.##..###.#...#...#.##....#####..#####....###..#.####.#...#.###.....#",
    "..#.####..#..#.#..#.######...##.##...##...#.#.#.....#..#...##..#.############.###.####....###..###..",
    "#.#...#.#.##..##..#.#..#...####.##.##.#.#.#.##..##.#.#.....#....#...#...#.###.#.#####..##.###...#..#",
    ".#....#.##..###.#..#.###.#..#.#..##..##.......########.#...#...#####.#...#..#..##.....#.##.....####.",
    "#.#####.#.##.###.#.#....#.#.###...##.#.....##..##..#.#####..#.#.##.#..###..##...#.#.##.#.#.....#.#..",
    "..###...#.#.......#.#......##.#..#.#.#.#.#...#.###.##...####....######......#...#####..###.##...#..#",
    "#..#...#..##..#...#...####.#...#....#####.#...#...#.#.....##...##..#...#....#..#####...#.....##...#.",
    "#.####.#...#...#..##...##....#...#.#.##.##.##...##..##.#..#..#.##.##.##.#.##......#.#...##.....#...#",
    ".#..####..###........#####...#....#.####..##..#####.##.###..#..###...##..##...##.....#..#.#.###.#...",
    ".#....#.####....#....##..#.#.######.#######.#.##.###.###...#.#....##..#..####.###.#....###...#.#....",
    "...###..##.#.##..#.#.#####.######.#..######.##...#.##.#..##.###.#.......#..#...#.###...##..####.##.#",
    "#....###....#..#####.#..#...###..##.##...##.###...#...#....#..#...#..####.#.####...#..##....#...#.##",
    "#.####.###...#..#.####...#..#.##.###.#.##.#....#..##.#.#...##.#..#.##.##..#####..#..#...###...#.####",
    "#.##.##..##.##......#.#.##...###.####.###.####.#...##...#.#...###..###.######.#####....###.####.#...",
    "##..#.###....#.#..###.#..##..###.#..##..#####.#.###..#.#...##.#.#.#.####....##...##....###.#.#.#..##",
    "...#.###.###..###.##...#.###.#.####.##..#.#..###...#..##.######.#.#..###..#.##...##.###....##.#...#.",
    "#..#.#..#.#..#.#.#.#.#..##..#....#..###.###.#...#.#####.#..#..#.#....#.#.#.#....##.##..#...##......#",
    "...#...##....#....#.##.######.#...#.....#.##..#....#..##.#.........###..#..#..#.##.##...#.#..#######",
    "##.##..#..#.#..#.#.######.##...####...#...#..#..##.#......#.#....#.###..#.###...#...#...#.##...###..",
    "#.####.#.##....##..###....#.##.#.##....####.#.#.##.#....#..#..###...#.....##.##....####..###........",
    "..#..##...##.#...#..#.#..###....##...#...####.....####....###..##..##..##.###..#.....######.........",
    ".###.###.##.#...#.##..##.#.##.#.#..#.#..###.#....###.#..##.###....#...#####.###..###.####..#.#...##.",
    "..##.#.#.####.#..#..###.##.#####.#.#....##..#.#.##..##..#...###.#...#...#...#...#..#..##.#...##...##",
    "......###..#####...##..##.#.....###.#...#..###..####..##..#..#####..##..#..##..####.#..#.........#..",
    "###............#.#.......###..#..##..#.#####.#.##.########.##..####.#.########..#.###.....#.####.#.#",
    ".#.....#....##..#.##..#...#.#.##.##..#.##...#.##.#..#......##.....##..##.#..##.###...###....#.##.###",
    "..#...###....##....#.#...###.###..##.##...#.#.#.#..#....###.#.##.....##.#..#.#######.#.###...###....",
    "##.#.#.#.#...####.##..#.#####..######..#.#...#.#.........#....##.....#....#.###....#.#.#..#...##....",
    ".......#.#.#..#....####.##.##.#.......#.#.###..#..#..#..##.#.#.##.#.##.#.#.#..##.#..###..#.###...##.",
    "..##.#.#..##.##...#..#..#..#..###..#.##..#.##..#..#....#....#.##.##.###.##.###..##.......######.###.",
    "##.#.#.#.#.#..###...###..####...##..##.###.#..#..####.#...###..#.##.##.#.#.###..###.#.#.#...###..#..",
    "..##...####......##..#..#..#...#...#..##...######.##......#.#.#....#.#.#.#..#..##.#...#.########...#",
    "####.##.#.#.####..#.#.##.#..#...#.#.##.#....#..#.####.#.#####.###..##.#.####...##.###.#.#....#.#####",
]

input = sample_input
algo = parse_image_enhancement_algo(input)
initial_image_dict = parse_image_grid(input)
act_initial_image_dict = parse_image_grid(actual_input)

print(f"{result_part1(actual_input)} should be 5179")
print(f"{result_part2(actual_input)} should be 16112")

# print(result_part1(input))
# print(result_part2(input))
