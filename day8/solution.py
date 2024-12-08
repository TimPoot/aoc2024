antenna_coords_dict: dict[str, list[tuple[int, int]]]= {}
anti_nodes: list[tuple[int, int]] = []

max_x: int
max_y: int

input_map: list[list[str]] = []

def print_map(anti_nodes: list[tuple[int, int]]):
    for i, line in enumerate(input_map):
        for j, point in enumerate(line):
            if (i, j) in anti_nodes and point == '.':
                print('#', end='')
            else:
                print(point, end='')

        print('')

with open('input.txt', 'r') as input_file:
    for i, line in enumerate(input_file):
        input_map += [[]]
        max_y = i
        max_x = len(line) - 1

        for j, point in enumerate(list(line.strip())):
            input_map[i] += point
            if point == '.':
                continue

            if point in antenna_coords_dict:
                antenna_coords_dict[point] += [(i, j)]
            else:
                antenna_coords_dict[point] = [(i, j)]

def part1(anti_nodes: list[tuple[int, int]]):
    for antenna_type in antenna_coords_dict:
        antennas_for_type = antenna_coords_dict[antenna_type]

        for i, current_antenna in enumerate(antennas_for_type):
            if i + 1 >= len(antennas_for_type):
                break

            for j in range(i + 1, len(antennas_for_type)):
                comparison_antenna = antennas_for_type[j]

                dist_x = current_antenna[0] - comparison_antenna[0]
                dist_y = current_antenna[1] - comparison_antenna[1]
                candidate_node_1 = (current_antenna[0] + dist_x, current_antenna[1] + dist_y)
                candidate_node_2 = (comparison_antenna[0] - dist_x, comparison_antenna[1] - dist_y)
                
                for candidate_node in [candidate_node_1, candidate_node_2]:
                    if candidate_node not in anti_nodes and candidate_node[0] >= 0 and candidate_node[0] <= max_x and candidate_node[1] >= 0 and candidate_node[1] <= max_y:
                        anti_nodes += [candidate_node]
    
    print(len(anti_nodes))

def part2(anti_nodes: list[tuple[int, int]]):
    for antenna_type in antenna_coords_dict:
        antennas_for_type = antenna_coords_dict[antenna_type]

        for i, current_antenna in enumerate(antennas_for_type):
            if current_antenna not in anti_nodes:
                anti_nodes += [current_antenna]

            if i + 1 >= len(antennas_for_type):
                break

            for j in range(i + 1, len(antennas_for_type)):
                comparison_antenna = antennas_for_type[j]

                dist_x = current_antenna[0] - comparison_antenna[0]
                dist_y = current_antenna[1] - comparison_antenna[1]
                
                for direction in [(dist_x, dist_y), (-dist_x, -dist_y)]:
                    counter = 0
                    candidate_node = (current_antenna[0] + direction[0] * counter, current_antenna[1] + direction[1] * counter)
                    while candidate_node[0] >= 0 and candidate_node[0] <= max_x and candidate_node[1] >= 0 and candidate_node[1] <= max_y:
                        if candidate_node not in anti_nodes:
                            anti_nodes += [candidate_node]

                        counter += 1
                        candidate_node = (current_antenna[0] + direction[0] * counter, current_antenna[1] + direction[1] * counter)

    print(len(anti_nodes))

part2(anti_nodes)