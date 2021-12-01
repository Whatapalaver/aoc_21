# Advent of Code - Day 1 - Part Two


def result(input):
    int_input = [int(i) for i in input]
    return sum(1 for a, b in zip(int_input, int_input[3:]) if b > a)
