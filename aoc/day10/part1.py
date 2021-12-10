# Advent of Code - Day 10 - Part One


def incorrect_closer(row):
    open_and_shut = {"(": ")", "[": "]", "{": "}", "<": ">"}

    openers = open_and_shut.keys()
    closers = open_and_shut.values()

    openers_stack = []

    for char in row:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return char
            else:
                last_unclosed_opener = openers_stack.pop()
                if not open_and_shut[last_unclosed_opener] == char:
                    return char
    return None


def score_invalid_closers(invalid_closers):
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}

    return sum([points[closer] for closer in invalid_closers])


def parse(input):
    return [[char for char in row] for row in input]


def result(input):
    data = parse(input)
    invalid_closers = []
    for row in data:
        char = incorrect_closer(row)
        if char is not None:
            invalid_closers.append(char)
    return score_invalid_closers(invalid_closers)


sample_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]
input = sample_input

# print(parse(input))
print(result(input))
