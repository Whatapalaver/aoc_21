# Advent of Code - Day 3 - Part One


def result(input):
    report_length = len(input)
    number_length = len(input[0])
    gamma_rate, epsilon_rate = "", ""

    for position in range(number_length):
        positional_bits = [int(list(number)[position]) for number in input]
        positional_sum = sum(positional_bits)
        if positional_sum > report_length / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)
