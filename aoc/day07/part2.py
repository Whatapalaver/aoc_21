# Advent of Code - Day 7 - Part Two


def parse(input):
    return [int(n) for n in input[0].split(",")]


def result(input):
    positions = parse(input)
    fuel_cost_options = []
    for i in range(min(positions), max(positions) + 1):
        fuel_total = 0
        for n in positions:
            move = abs(n - i)
            fuel = move * (move + 1) / 2
            fuel_total += fuel
        fuel_cost_options.append(fuel_total)
    return min(fuel_cost_options)


sample_input = ["16,1,2,0,4,2,7,1,2,14"]
input = sample_input

print(result(input))
