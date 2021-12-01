# Advent of Code - Day 1 - Part One


def result(input):
    int_input = [int(i) for i in input]
    comparator = int_input[0]
    accumulator = 0
    for i in int_input:
        if i > comparator:
            accumulator += 1
        comparator = i
    return accumulator


def alt_zip_result(input):
    int_input = [int(i) for i in input]
    count = 0
    for a, b in zip(int_input, int_input[1:]):
        if b > a:
            count += 1
    return count


def alt_zip_sum_result(input):
    int_input = [int(i) for i in input]
    return sum(1 for a, b in zip(int_input, int_input[1:]) if b > a)
