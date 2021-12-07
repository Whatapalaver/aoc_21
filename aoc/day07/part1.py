# Advent of Code - Day 7 - Part One


def parse(input):
    return [int(n) for n in input[0].split(",")]


def result(input):
    positions = parse(input)
    fuel_cost_options = []
    for i in range(min(positions), max(positions) + 1):
        movements = [abs(n - i) for n in positions]
        fuel_cost_options.append(sum(movements))
    return min(fuel_cost_options)


sample_input = ["16,1,2,0,4,2,7,1,2,14"]
input = sample_input

print(result(input))
