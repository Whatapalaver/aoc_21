# Advent of Code - Day 2 - Part Two

def result(input):
    sep_input = [str.split() for str in input]
    aim, x, y = 0, 0, 0
    for dir, val in sep_input:
        match dir:
            case 'forward':
                x += int(val)
                y += int(val) * aim
            case 'down':
                aim += int(val)
            case 'up':
                aim -= int(val)
    
    return x * y
