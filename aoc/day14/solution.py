# Advent of Code - Day 14

from collections import defaultdict, Counter
from itertools import pairwise


def get_recipe(recipe_row):
    return [n for n in recipe_row]


def get_insertion_instruction(data):
    instruction = {}
    for row in data:
        x, y = row.split(" -> ")
        instruction[x] = y
    return instruction


def parse(input):
    recipe = get_recipe(input[0])
    instructions = get_insertion_instruction(input[2:])
    return recipe, instructions


def insert(polymer, instructions):
    new_polymer = [polymer[0]]
    for x, y in pairwise(polymer):
        # print(f"Pairs: {x},{y}")
        insert = instructions[x + y]
        # print(f"Insert: {insert}")
        new_polymer.append(insert + y)
    # print(f"Iterated polymer: {new_polymer}")
    return "".join(new_polymer)


def score(polymer):
    c = Counter(polymer)
    most_freq_count = c.most_common(1)[0][1]
    least_freq_count = c.most_common()[-1][1]
    print(f"Counter: {c}")
    print(f"Most freq val: {most_freq_count}")
    print(f"Least freq val: {least_freq_count}")
    return most_freq_count - least_freq_count


def result_part1(input, steps=10):
    recipe, instructions = parse(input)
    polymer = recipe
    for step in range(steps):
        polymer = insert(polymer, instructions)
        print(f"At step {step}, plymer length is {len(polymer)}")

    return score(polymer)


def insert_part2(polymer_pairs, instructions):
    new_poly_pairs = defaultdict(int)
    for pair, count in polymer_pairs.items():
        insert = instructions[pair]
        if insert:
            new_poly_pairs[pair[0] + insert] += count
            new_poly_pairs[insert + pair[1]] += count
        else:
            new_poly_pairs[pair] += count
        polymer_pairs = new_poly_pairs

    return new_poly_pairs


# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB


def result_part2(input, steps=40):
    recipe, instructions = parse(input)
    new_polymer_pairs = defaultdict(int)
    for x, y in pairwise(recipe):
        new_polymer_pairs[x + y] += 1
    for _ in range(steps):
        new_polymer_pairs = insert_part2(new_polymer_pairs, instructions)
        # print(f"At step {step}, polymer pairs {new_polymer_pairs}")

    counts = defaultdict(int)
    for pair, count in new_polymer_pairs.items():
        counts[pair[0]] += count

    # account for tail of polymer
    counts[recipe[-1]] += 1

    return new_polymer_pairs, max(counts.values()) - min(counts.values())


sample_input = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]

input = sample_input

# print(result_part1(input))
# print(result_part2(input))
