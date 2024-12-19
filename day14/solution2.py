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

def does_robot_have_neighbour(current_robot, all_robots):
    current_x = current_robot[0][0]
    current_y = current_robot[0][1]
    
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == 0 and j == 0:
                continue
            if any(robot[0][0] == current_x + i and robot[0][1] == current_y + j for robot in all_robots):
                return True

    return False

for i in range(999999):
    for robot in robots:
        new_x = robot[0][0] + robot[1][0]
        new_y = robot[0][1] + robot[1][1]
        robot[0] = (robot[0][0] + robot[1][0], robot[0][1] + robot[1][1])

    if sum(does_robot_have_neighbour(robot, robots) for robot in robots) / len(robots) >= 0.65:
        print(f"!!!!! Found possibility: {i} !!!!!")

    if i % 1000 == 0:
        print(f"Update: {i}")
