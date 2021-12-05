# Advent of Code - Day 4 - Part One


def reset_board():
    return [[], [[] for i in range(5)]]


def parse(input):
    """returns number and boards.
    Boards is a list of each board which in turn is a list of rows and columns"""
    numbers = [int(num) for num in input[0].split(",")]
    boards = []
    board = reset_board()  # a board holds rows and cols
    for line in input[2:]:
        if len(line.strip()) == 0:
            boards.append(board)
            board = reset_board()
        else:
            # create rows
            row = [int(num) for num in line.split()]
            board[0].append(row)
            # now deal with cols
            index = 0
            for n in row:
                board[1][index].append(n)
                index += 1
    boards.append(board)  # append last board
    return numbers, boards


def check_array(arrays, nums):
    """Array can be either row or column"""
    for array in arrays:  # for row in rows or col in cols
        win = all(i in nums for i in array)
        if win:
            return True
    return False


def winning_result(rows, called_nums):
    relevant_total = sum([i for row in rows for i in row if i not in called_nums])
    last_called = called_nums[-1]
    return relevant_total * last_called


def result(input):
    nums, boards = parse(input)
    called_nums = nums[:5]

    for num in nums[5:]:
        called_nums.append(num)
        for board in boards:
            rows = board[0]
            cols = board[1]
            if check_array(rows, called_nums) | check_array(cols, called_nums):
                return winning_result(rows, called_nums)
