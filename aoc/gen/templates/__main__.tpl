#!/usr/bin/env python3

from pathlib import Path

from aoc.$module_name import part1, part2

def read_file(filename):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        lines = f.read().splitlines()
        return lines

def main():
    input1 = read_file("./resources/input.txt")
    input2 = read_file("./resources/input2.txt")

    print("--- Part One ---")
    print("Result:", part1.result(input1))

    print("--- Part Two ---")
    print("Result:", part2.result(input2))

if __name__ == "__main__":
    main()
