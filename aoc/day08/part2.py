# Advent of Code - Day 8 - Part Two

from collections import Counter, defaultdict

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
        sorted_signals = ["".join(sorted(code)) for code in signal.split()]
        sorted_outputs = ["".join(sorted(code)) for code in output.split()]
        data.append([sorted(sorted_signals, key=len), sorted_outputs])
    return data


def def_value():
    return "TBC"


def containsAll(substring, string):
    for letter in set(substring):
        if letter not in set(string):
            return False
    return True


def substringRemainder(substring, string):
    mismatch = 0
    for letter in set(substring):
        if letter not in set(string):
            mismatch += 1
    return mismatch


def crack_sixes(one, four, len_sixes):
    nine = [sixer for sixer in len_sixes if containsAll(four, sixer)][0]
    len_sixes.remove(nine)
    zero = [sixer for sixer in len_sixes if containsAll(one, sixer)][0]
    len_sixes.remove(zero)
    six = len_sixes[0]

    return zero, six, nine


def crack_fives(one, six, len_fives):
    three = [fiver for fiver in len_fives if containsAll(one, fiver)][0]
    len_fives.remove(three)
    # five is closer to six than two is to six
    five = [fiver for fiver in len_fives if substringRemainder(six, fiver) == 1][0]
    len_fives.remove(five)
    two = len_fives[0]
    return two, three, five


def initialise_dict(signal):
    lookup = {
        0: "TBC",
        1: signal[0],
        2: "TBC",
        3: "TBC",
        4: signal[2],
        5: "TBC",
        6: "TBC",
        7: signal[1],
        8: signal[9],
        9: "TBC",
    }

    return lookup


def generate_full_lookup(signals):
    len_sixes = [code for code in signals if len(code) == 6]
    len_fives = [code for code in signals if len(code) == 5]
    lookup_table = initialise_dict(signals)
    zero, six, nine = crack_sixes(lookup_table[1], lookup_table[4], len_sixes)
    lookup_table[0] = zero
    lookup_table[6] = six
    lookup_table[9] = nine
    two, three, five = crack_fives(lookup_table[1], lookup_table[6], len_fives)
    lookup_table[2] = two
    lookup_table[3] = three
    lookup_table[5] = five
    return lookup_table


def output_value(outputs, lookup_table):
    inv_lookup = {v: k for k, v in lookup_table.items()}
    str_val = ["".join(str(inv_lookup[code]) for code in outputs)]
    return int(str_val[0])


def result(input):
    data = parse(input)
    result = 0
    for line in data:
        signals = line[0]
        outputs = line[1]
        lookup_table = generate_full_lookup(signals)
        value = output_value(outputs, lookup_table)
        result += value
    return result
