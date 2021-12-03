from aoc.day03 import part1, part2

#
# --- Part One ---
#

test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_part1():
    assert part1.result(test_input) == 198


#
# --- Part Two ---
#


def test_part2():
    assert part2.result(test_input) == 230
