# Advent of Code - Day 10


def parse(input):
    return [[char for char in row] for row in input]


def corrupt_closer(open_and_shut, row):
    """Returns boolean indicating corruptness and first corrupt closer"""
    openers = open_and_shut.keys()
    closers = open_and_shut.values()

    openers_stack = []

    for char in row:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return True, char
            else:
                last_unclosed_opener = openers_stack.pop()
                if not open_and_shut[last_unclosed_opener] == char:
                    return True, char
    return False, None


def score_invalid_closers(invalid_closers):
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}

    return sum([points[closer] for closer in invalid_closers])


def result_part1(input):
    data = parse(input)
    open_and_shut = {"(": ")", "[": "]", "{": "}", "<": ">"}
    invalid_closers = []
    for row in data:
        corrupt, char = corrupt_closer(open_and_shut, row)
        if corrupt:
            invalid_closers.append(char)
    return score_invalid_closers(invalid_closers)


def incorrect_open_close(open_and_shut, row):
    opener_keys = open_and_shut.keys()
    closer_keys = open_and_shut.values()
    openers_stack = []
    invalid_closer = []
    for char in row:
        if char in opener_keys:
            openers_stack.append(char)
        elif char in closer_keys:
            if not openers_stack:
                invalid_closer.append(char)
            else:
                last_unclosed_opener = openers_stack.pop()
                if not open_and_shut[last_unclosed_opener] == char:
                    invalid_closer.append(char)
    return invalid_closer, openers_stack


def score_unmatched_openers(matching_pairs, unmatched_openers):
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    missing_closers = [matching_pairs[opener] for opener in unmatched_openers]
    missing_closers.reverse()
    total_score = 0
    for closer in missing_closers:
        total_score *= 5
        total_score += points[closer]
    return total_score


def result_part2(input):
    data = parse(input)
    open_and_shut = {"(": ")", "[": "]", "{": "}", "<": ">"}

    scores = []
    for row in data:
        invalid_closer, unmatched_openers = incorrect_open_close(open_and_shut, row)
        if invalid_closer:
            continue
        else:
            scores.append(score_unmatched_openers(open_and_shut, unmatched_openers))
    scores.sort(reverse=True)
    middle_score = scores[int(len(scores) / 2)]
    return middle_score


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
print(result_part1(input))
print(result_part2(input))
