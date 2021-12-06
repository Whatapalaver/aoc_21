# Advent of Code - Day 6 - Part Two


class LanterFishPopulation:
    def __init__(self, initial_state):
        self.population = initial_state

    def tick(self, reset, gestation):
        spawn_count = self.population[0]
        # decrement all lantern fish timers
        for k in self.population.keys():
            if k < gestation:
                self.population[k] = self.population[k + 1]

        # deal with regenerating lantern fish
        self.population[reset] += spawn_count
        # spawn the new generation
        self.population[gestation] = spawn_count


def parse(line):
    return [int(num) for num in line[0].split(",")]


def result(input, reset=6, gestation=8, cycles=256):
    initial_state = dict.fromkeys(range(gestation + 1), 0)
    periods = parse(input)
    for n in periods:
        initial_state[n] += 1

    lfp = LanterFishPopulation(initial_state)
    for n in range(cycles):
        lfp.tick(reset, gestation)
    return sum(lfp.population.values())


sample_input = ["3,4,3,1,2"]
input = sample_input
print(result(input, cycles=18))
# print(result(input, cycles = 80))
# print(result(input, cycles = 256))
