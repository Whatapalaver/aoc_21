from aoc.day01 import part1, part2

#
# --- Part One ---
#
sample_input = ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]


def test_part1():
    assert part1.result(sample_input) == 7
    assert part1.alt_zip_result(sample_input) == 7
    assert part1.alt_zip_sum_result(sample_input) == 7


#
# --- Part Two ---
#


def test_part2():
    assert part2.result(sample_input) == 5
