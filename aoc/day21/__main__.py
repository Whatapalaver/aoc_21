#!/usr/bin/env python3

from pathlib import Path

from aoc.day21 import solution

def read_file(filename):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        lines = f.read().splitlines()
        return lines

def main():
    input = read_file("./resources/input.txt")

    print("--- Part One ---")
    print("Result:", solution.result_part1(input))

    print("--- Part Two ---")
    print("Result:", solution.result_part2(input))

if __name__ == "__main__":
    main()