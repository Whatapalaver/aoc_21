# Advent of Code - Day 2 - Part One


def result(input):
    sep_input = [str.split() for str in input]
    directional_dict = {"up": 0, "down": 0, "forward": 0}
    for dir, val in sep_input:
        directional_dict[dir] += int(val)

    x = directional_dict["forward"]
    y = directional_dict["down"] - directional_dict["up"]
    return x * y
