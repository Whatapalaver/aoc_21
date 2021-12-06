# Advent of Code - Day 6 - Part One


class LanterFishPopulation:
    def __init__(self, initial_state=[]):
        self.population = initial_state

    def spawn(self, gestation=8):
        self.population.append(gestation)

    def tick(self, reset=6):
        spawn_count = 0
        # decrement or reset all lantern fish timers
        for idx, val in enumerate(self.population):
            if val == 0:
                self.population[idx] = reset
                spawn_count += 1
            else:
                self.population[idx] -= 1
        # spawn new fish for all rest lantern fish
        for n in range(spawn_count):
            self.spawn()


def parse(line):
    return [int(num) for num in line[0].split(",")]


def result(input, cycles=80):
    initial_state = parse(input)
    lfp = LanterFishPopulation(initial_state)
    for n in range(cycles):
        lfp.tick()
    print(lfp.population)
    return len(lfp.population)
