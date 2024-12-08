obstacles_list: list[tuple[int, int]] = []

begin_position: tuple[int, int]
current_position: tuple[int, int]

# 0 = up, 1 = right, 2 = down, 3 = left, 4 = uh oh
current_direction: int = 0

visited_spaces: list[tuple[int, int]] = []
possible_obstacles: list[tuple[int, int]] = []
visited_spaces_direction: list[tuple[int, int, int]] = []

input_map: list[list[int]] = []

with open('input.txt', 'r') as input_file:
    for i, line in enumerate(input_file):
        input_map += [[]]

        for j, place in enumerate(list(line.strip())):
            input_map[i] += [place]

            if place == '#':
                obstacles_list += [(i, j)]
            if place == '^':
                current_position = (i, j)
                begin_position = (i, j)

def print_current_pos():
    print('=== MAP ===')
    for i, line in enumerate(input_map):
        for j, point in enumerate(line):
            if (i, j) == current_position:
                print('@', end='')
            elif (i,j) in visited_spaces:
                print('X', end='')
            else:
                print(point, end='')

        print('')

def print_current_pos2(new_obstacle: tuple[int, int], visited_spaces_direction: list[tuple[int, int, int]]):
    visited_spaces_no_direction = list(map(lambda x: (x[0], x[1]), visited_spaces_direction))

    print('=== MAP ===')
    for i, line in enumerate(input_map):
        for j, point in enumerate(line):
            if (i, j) == current_position:
                print('@', end='')
            elif  (i,j) in visited_spaces_no_direction:
                print('X', end='')
            elif (i, j) == new_obstacle:
                print('O', end='')
            else:
                print(point, end='')

        print('')

def part1(current_position: tuple[int, int], obstacles_list: list[tuple[int, int]], visited_spaces: list[tuple[int, int]], current_direction: int) -> list[tuple[int, int]]:
    is_in_bounds: bool = True
    while is_in_bounds:
        obstacles_in_path: list[int] = []
        nearest_obstacle: int

        match current_direction:
            case 0:
                # Going up, x decrease
                obstacles_in_path = [obstacle[0] for obstacle in obstacles_list if obstacle[1] == current_position[1] and obstacle[0] < current_position[0]]

                if obstacles_in_path == []:
                    is_in_bounds = False
                    nearest_obstacle = 0
                else:
                    nearest_obstacle = max(obstacles_in_path)

                visited_spaces += [(x,current_position[1]) for x in range(current_position[0], nearest_obstacle, -1) if (x,current_position[1]) not in visited_spaces]
                current_position = (nearest_obstacle+1, current_position[1])

            case 1:
                # Going right, y increase
                obstacles_in_path = [obstacle[1] for obstacle in obstacles_list if obstacle[0] == current_position[0] and obstacle[1] > current_position[1]]

                if obstacles_in_path == []:
                    is_in_bounds = False
                    nearest_obstacle = len(input_map[0])-1
                else:
                    nearest_obstacle = min(obstacles_in_path)

                visited_spaces += [(current_position[0],y) for y in range(current_position[1], nearest_obstacle, 1) if (current_position[0],y) not in visited_spaces]
                current_position = (current_position[0], nearest_obstacle-1)

            case 2:
                # Going down, x increase
                obstacles_in_path = [obstacle[0] for obstacle in obstacles_list if obstacle[1] == current_position[1] and obstacle[0] > current_position[0]]

                if obstacles_in_path == []:
                    is_in_bounds = False
                    nearest_obstacle = len(input_map)-1
                else:
                    nearest_obstacle = min(obstacles_in_path)

                visited_spaces += [(x,current_position[1]) for x in range(current_position[0], nearest_obstacle, 1) if (x,current_position[1]) not in visited_spaces]
                current_position = (nearest_obstacle-1, current_position[1])

            case 3:
                # Going left, y decrease
                obstacles_in_path = [obstacle[1] for obstacle in obstacles_list if obstacle[0] == current_position[0] and obstacle[1] < current_position[1]]

                if obstacles_in_path == []:
                    is_in_bounds = False
                    nearest_obstacle = 0
                else:
                    nearest_obstacle = max(obstacles_in_path)

                visited_spaces += [(current_position[0],y) for y in range(current_position[1], nearest_obstacle, -1) if (current_position[0],y) not in visited_spaces]
                current_position = (current_position[0], nearest_obstacle+1)

            case _:
                # Going down, the bad kind
                print("~~ UH OH ~~")

        current_direction = (current_direction + 1) % 4

    print(f'Amount of spaces visited: {len(visited_spaces)+1}')
    return visited_spaces
    
possible_obstacles = part1(current_position, obstacles_list, visited_spaces, current_direction)
possible_obstacles.remove(begin_position)

loops_found = 0
for possible_obstacle in possible_obstacles:
    current_direction = 0
    current_position = begin_position
    visited_spaces_direction = []
    obstacles_attempt = obstacles_list + [possible_obstacle]

    while True:
        obstacles_in_path: list[int] = []
        nearest_obstacle: int

        match current_direction:
            case 0:
                # Going up, x decrease
                obstacles_in_path = [obstacle[0] for obstacle in obstacles_attempt if obstacle[1] == current_position[1] and obstacle[0] < current_position[0]]

                if obstacles_in_path == []:
                    break
                else:
                    nearest_obstacle = max(obstacles_in_path)

                visited_spaces_direction += [(x,current_position[1],current_direction) for x in range(current_position[0], nearest_obstacle, -1)]
                if len(visited_spaces_direction) != len(set(visited_spaces_direction)):
                    # print_current_pos2(possible_obstacle, visited_spaces_direction)
                    loops_found += 1
                    break

                current_position = (nearest_obstacle+1, current_position[1])

            case 1:
                # Going right, y increase
                obstacles_in_path = [obstacle[1] for obstacle in obstacles_attempt if obstacle[0] == current_position[0] and obstacle[1] > current_position[1]]

                if obstacles_in_path == []:
                    break
                else:
                    nearest_obstacle = min(obstacles_in_path)

                visited_spaces_direction += [(current_position[0],y,current_direction) for y in range(current_position[1], nearest_obstacle, 1)]
                if len(visited_spaces_direction) != len(set(visited_spaces_direction)):
                    # print_current_pos2(possible_obstacle, visited_spaces_direction)
                    loops_found += 1
                    break

                current_position = (current_position[0], nearest_obstacle-1)

            case 2:
                # Going down, x increase
                obstacles_in_path = [obstacle[0] for obstacle in obstacles_attempt if obstacle[1] == current_position[1] and obstacle[0] > current_position[0]]

                if obstacles_in_path == []:
                    break
                else:
                    nearest_obstacle = min(obstacles_in_path)

                visited_spaces_direction += [(x,current_position[1],current_direction) for x in range(current_position[0], nearest_obstacle, 1)]
                if len(visited_spaces_direction) != len(set(visited_spaces_direction)):
                    # print_current_pos2(possible_obstacle, visited_spaces_direction)
                    loops_found += 1
                    break

                current_position = (nearest_obstacle-1, current_position[1])

            case 3:
                # Going left, y decrease
                obstacles_in_path = [obstacle[1] for obstacle in obstacles_attempt if obstacle[0] == current_position[0] and obstacle[1] < current_position[1]]

                if obstacles_in_path == []:
                    break
                else:
                    nearest_obstacle = max(obstacles_in_path)

                visited_spaces_direction += [(current_position[0],y,current_direction) for y in range(current_position[1], nearest_obstacle, -1)]
                if len(visited_spaces_direction) != len(set(visited_spaces_direction)):
                    # print_current_pos2(possible_obstacle, visited_spaces_direction)
                    loops_found += 1
                    break

                current_position = (current_position[0], nearest_obstacle+1)

            case _:
                # Going down, the bad kind
                print("~~ UH OH ~~")

        current_direction = (current_direction + 1) % 4

print(f'Infinte loops found: {loops_found}')