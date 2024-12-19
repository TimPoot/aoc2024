import re
import numpy as np

# it costs 3 tokens to push the A button and 1 token to push the B button.
# What is the fewest tokens you would have to spend to win all possible prizes?
# It is possible that there is no solution for a problem

# A single machine is a tuple of the dA, dB and the target
machines = []

regex = r"X[\+\=](\d+), Y[\+\=](\d+)"

current_x = np.array([])
current_y = np.array([])
current_finish = np.array([])
with open("input.txt", "r") as input_file:
    for line in input_file:
        matches = re.search(regex, line)
        if matches == None:
            machines += [[current_x, current_y, current_finish]]
            current_x = np.array([])
            current_y = np.array([])
            current_finish = np.array([])
            continue

        groups = np.array(list(map(int, matches.groups())))
        if "Button A" in line:
            current_x = np.append(current_x, int(groups[0]))
            current_y = np.append(current_y, int(groups[1]))
        elif "Button B" in line:
            current_x = np.append(current_x, int(groups[0]))
            current_y = np.append(current_y, int(groups[1]))
        elif "Prize" in line:
            current_finish = np.array(groups)
        else:
            print("!!! HUH !!!")
machines += [[current_x, current_y, current_finish]]

def is_not_floating_point_bs(x, y, solution, target):
    # print(f"X times solution is: {np.dot(x, solution)} Should be : {solution[0]}")
    # print(target)
    return np.dot(x, solution) == target[0] and np.dot(y, solution) == target[1]

total_tokens = 0
for machine in machines:
    target_b = np.array([val + 10000000000000 for val in machine[2]])
    solution = np.linalg.solve(np.array([machine[0], machine[1]]), target_b)
    # print(solution)
    if is_not_floating_point_bs(machine[0], machine[1], np.array([round(val) for val in solution]), target_b):
        total_tokens += 3 * solution[0] + solution[1]

print(total_tokens)