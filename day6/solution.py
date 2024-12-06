obstacles_list: list[tuple[int, int]] = []

current_position: tuple[int, int]

# 0 = up, 1 = right, 2 = down, 3 = left, 4 = uh oh
current_direction: int = 0

visited_spaces: list[tuple[int, int]] = []

map: list[list[int]] = []

with open('input.txt', 'r') as input_file:
    for i, line in enumerate(input_file):
        map += [[]]

        for j, place in enumerate(list(line.strip())):
            map[i] += [place]

            if place == '#':
                obstacles_list += [(i, j)]
            if place == '^':
                current_position = (i, j)

def print_current_pos():
    print('=== MAP ===')
    for i, line in enumerate(map):
        for j, point in enumerate(line):
            if (i, j) == current_position:
                print('@', end='')
            elif (i,j) in visited_spaces:
                print('X', end='')
            else:
                print(point, end='')

        print('')

is_in_bounds: bool = True
while is_in_bounds:
    obstacles_in_path: list[int] = []
    nearest_obstacle: int

    match current_direction:
        case 0:
            # Going up, x decrease
            obstacles_in_path = [obstacle[0] for obstacle in obstacles_list if obstacle[1] == current_position[1] and obstacle[0] < current_position[0]]

            if obstacles_in_path == []:
                print('OOB')
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
                print('OOB')
                is_in_bounds = False
                nearest_obstacle = len(map[0])-1
            else:
                nearest_obstacle = min(obstacles_in_path)

            visited_spaces += [(current_position[0],y) for y in range(current_position[1], nearest_obstacle, 1) if (current_position[0],y) not in visited_spaces]
            current_position = (current_position[0], nearest_obstacle-1)

        case 2:
            # Going down, x increase
            obstacles_in_path = [obstacle[0] for obstacle in obstacles_list if obstacle[1] == current_position[1] and obstacle[0] > current_position[0]]

            if obstacles_in_path == []:
                print('OOB')
                is_in_bounds = False
                nearest_obstacle = len(map)-1
            else:
                nearest_obstacle = min(obstacles_in_path)

            visited_spaces += [(x,current_position[1]) for x in range(current_position[0], nearest_obstacle, 1) if (x,current_position[1]) not in visited_spaces]
            current_position = (nearest_obstacle-1, current_position[1])

        case 3:
            # Going left, y decrease
            obstacles_in_path = [obstacle[1] for obstacle in obstacles_list if obstacle[0] == current_position[0] and obstacle[1] < current_position[1]]

            if obstacles_in_path == []:
                print('OOB')
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
    # print(obstacles_in_path)
    # print_current_pos()
    
# print_current_pos()
print(len(visited_spaces)+1)