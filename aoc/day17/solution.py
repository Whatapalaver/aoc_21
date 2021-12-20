# Advent of Code - Day 17
import re


def parse(input):
    m = re.search(
        r"x=(?P<x1>\d+)..(?P<x2>\d+), y=(?P<y1>\d+|-\d+)..(?P<y2>\d+|-\d+)", input[0]
    )
    return (
        int(m.group("x1")),
        int(m.group("x2")),
        int(m.group("y1")),
        int(m.group("y2")),
    )


def result_part1(input):
    xmin, xmax, ymin, ymax = parse(input)
    # print(f"xmin: {xmin}, xmax: {xmax}, ymin: {ymin}, ymax: {ymax}")
    # start with a reasonable min
    max_height = ymin

    # For every reasonable (initial_x_vel, initial_y_val)
    for initial_x_vel in range(1, xmax + 1):
        for initial_y_vel in range(ymin, -ymin):
            x, y = 0, 0
            vx, vy = initial_x_vel, initial_y_vel
            shot_peak = ymin
            # Unless position out of bounds
            while x <= xmax and y >= ymin:
                # If target hit
                if x >= xmin and y <= ymax:
                    if shot_peak > max_height:
                        max_height = shot_peak
                    break

                # Apply rules
                x, y = (x + vx, y + vy)  # increment psoition
                vy -= 1  # decrement velocity
                if y > shot_peak:
                    shot_peak = y
                # vx can never go below 0
                if vx > 0:
                    vx -= 1

    return max_height


def result_part2(input):
    xmin, xmax, ymin, ymax = parse(input)
    total = 0

    # For every reasonable (initial_x_vel, initial_y_val)
    for initial_x_vel in range(1, xmax + 1):
        for initial_y_vel in range(ymin, -ymin):
            x, y = 0, 0
            vx, vy = initial_x_vel, initial_y_vel

            # While we did not get past the target (on either axis)
            while x <= xmax and y >= ymin:
                # If we are inside the target, these v0x and v0y were good
                if x >= xmin and y <= ymax:
                    total += 1
                    break

                # Advance the trajectory following the rules
                x, y = (x + vx, y + vy)
                vy -= 1

                if vx > 0:  # ... also remembering that vx can never go below 0
                    vx -= 1

    return total


sample_input = ["target area: x=20..30, y=-10..-5"]
input = sample_input

# print(parse(input))
# print(result_part1(input))
