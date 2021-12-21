# Advent of Code - Day 21
sample_input = [4, 8]
actual_input = [3, 10]

input = actual_input


def in_play(scores):
    return scores[0] < 1000 and scores[1] < 1000


def result(scores, rolls):
    return min(scores) * rolls


def result_part1(input):
    # with deterministic dice
    positions = input
    scores = [0, 0]

    die = 0
    rolls = 0
    player_turn = 0  # flip between 0 and 1 for player 1 and 2

    while in_play(scores):
        turn_rolls = []
        for _ in range(3):
            die = die % 100 + 1
            turn_rolls.append(die)
            rolls += 1
        positions[player_turn] = (positions[player_turn] + sum(turn_rolls) - 1) % 10 + 1
        scores[player_turn] += positions[player_turn]
        # print(
        #     f"Player {player_turn} rolls {str(turn_rolls)} and moves to space {positions[player_turn]} for score of {scores[player_turn]}"
        # )

        # toggle player
        player_turn = int(not (player_turn))

    print(scores)
    print(rolls)
    return result(scores, rolls)


def result_part2(input):
    # with dirac dice
    positions = input
    scores = [0, 0]

    die = 0
    rolls = 0
    player_turn = 0  # flip between 0 and 1 for player 1 and 2

    while in_play(scores):
        turn_rolls = []
        for _ in range(3):
            die = die % 100 + 1
            turn_rolls.append(die)
            rolls += 1
        positions[player_turn] = (positions[player_turn] + sum(turn_rolls) - 1) % 10 + 1
        scores[player_turn] += positions[player_turn]
        # print(
        #     f"Player {player_turn} rolls {str(turn_rolls)} and moves to space {positions[player_turn]} for score of {scores[player_turn]}"
        # )

        # toggle player
        player_turn = int(not (player_turn))

    print(scores)
    print(rolls)
    return result(scores, rolls)


print(result_part1(input))
