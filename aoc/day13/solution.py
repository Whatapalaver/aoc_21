# Advent of Code - Day 13


def parse(input):
    sheet = set()
    folds = []
    for row in input:
        if row == "":
            break

        coords = tuple(map(int, row.split(",")))
        sheet.add(coords)
    instructions = [row for row in input if row[0:4] == "fold"]
    for row in instructions:
        axis = int(row[row.index("=") + 1 :])
        direction = row[row.index("=") - 1 : row.index("=")]
        folds.append((direction, axis))
    return sheet, folds


def fold(sheet, axis, direction):
    folded_sheet = set()
    for x, y in sheet:
        if direction == "y":  # vertical
            if y > axis:
                y = axis - (y - axis)
        elif x > axis:
            x = axis - (x - axis)
        folded_sheet.add((x, y))
    return folded_sheet


def display(sheet):
    max_x = max([x for x, _ in sheet])
    max_y = max([y for _, y in sheet])

    output = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            output += "#" if (x, y) in sheet else " "
        output += "\n"

    print(output)


def result_part1(input):
    sheet, folds = parse(input)
    first_fold = fold(sheet, folds[0][1], folds[0][0])
    print(first_fold)
    return len(first_fold)


def result_part2(input):
    sheet, folds = parse(input)
    for dir, axis in folds:
        sheet = fold(sheet, axis, dir)
    display(sheet)


sample_input = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]

# input = sample_input
# print(parse(input))
# print(result_part1(input))
# print(result_part2(input))
