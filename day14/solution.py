import re
import math

MAX_X = 101
MAX_Y = 103

regex = r"\=(\d+),(\d+).+\=(-?\d+),(-?\d+)"

# Robot is list of two tuples, each containg two intes: pos and vel
robots: list[list[tuple[int, int], tuple[int, int]]] =[]

with open("input.txt", "r") as input_file:
    for line in input_file:
        matches = [int(group) for group in re.search(regex, line).groups()]
        robots += [[(matches[0], matches[1]), (matches[2], matches[3])]]

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot in robots:
    final_x = (robot[0][0] + 100 * robot[1][0]) % MAX_X
    final_y = (robot[0][1] + 100 * robot[1][1]) % MAX_Y
    robot[0] = (final_x, final_y)

    if final_x == MAX_X // 2 or final_y == MAX_Y // 2:
        continue
    elif final_x < MAX_X // 2 and final_y < MAX_Y // 2:
        q1 += 1
    elif final_x > MAX_X // 2 and final_y > MAX_Y // 2:
        q4 += 1
    elif final_x > MAX_X // 2 and final_y < MAX_Y // 2:
        q2 += 1
    elif final_x < MAX_X // 2 and final_y > MAX_Y // 2:
        q3 += 1

print(q1 * q2 * q3 * q4)