# Advent of Code - Day 8 - Part One

from collections import Counter

# Unique patterns

# 0 -> 6
# 1 -> 2 *
# 2 -> 5
# 3 -> 5
# 4 -> 4 *
# 5 -> 5
# 6 -> 6
# 7 -> 3 *
# 8 -> 7 *
# 9 -> 6


def parse(input):
    data = []
    for line in input:
        signal, output = line.split(" | ")
        data.append([signal.split(), output.split()])
    return data


def result(input):
    data = parse(input)
    freq = Counter()
    for line in data:
        output_lengths = [len(code) for code in line[1]]
        print(output_lengths)
        freq.update(output_lengths)
    return freq[2] + freq[3] + freq[4] + freq[7]


sample_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]
input = sample_input
# print(parse(input))

print(result(input))
