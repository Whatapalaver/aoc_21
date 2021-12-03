# Advent of Code - Day 3 - Part Two


def process(input, position=0, commonest=True):
    zero_starts = [number for number in input if list(number)[position] == "0"]
    one_starts = [number for number in input if list(number)[position] == "1"]
    if len(zero_starts) > len(one_starts):
        if commonest:
            input = zero_starts
        else:
            input = one_starts
    else:
        if commonest:
            input = one_starts
        else:
            input = zero_starts
    return input


def extract_rating(input, commonest=True):
    position = 0
    rev_input = input
    while len(rev_input) > 1:
        rev_input = process(rev_input, position, commonest)
        position += 1
    return rev_input


def result(input):
    o2_rating = extract_rating(input, True)
    co2_rating = extract_rating(input, False)
    result = int(co2_rating[0], 2) * int(o2_rating[0], 2)
    return result
