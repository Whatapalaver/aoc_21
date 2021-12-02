from aoc.day02 import part1, part2

#
# --- Part One ---
#

sample_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_part1():
    assert part1.result(sample_input) == 150


#
# --- Part Two ---
#


def test_part2():
    assert part2.result(sample_input) == 900
