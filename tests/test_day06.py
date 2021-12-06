from aoc.day06 import part1, part2

sample_input = ["3,4,3,1,2"]

# --- Part One ---
#


def test_part1():
    assert part1.result(sample_input, cycles=18) == 26
    assert part1.result(sample_input, cycles=80) == 5934


#
# --- Part Two ---
#


def test_part2():
    assert part2.result(sample_input, cycles=256) == 26984457539
