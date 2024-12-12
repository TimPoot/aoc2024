# Houd een set bij van tuples die al in een blob zitten
# Een blob zelf is een set aan: (x,y), aantal_buren

directions_neighbours: list[tuple[int, int]] = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

map_values: list[list[str]] = []
map_visited: list[list[bool]] = []

# Point = ((x, y), #neighbours)
regions: list[list[tuple[tuple[int, int], list[tuple[int, int]]]]] = []

def print_map(input_map) -> None:
    for line in input_map:
        for value in line:
            print(value, end='')
        print('')

with open("input.txt", "r") as input_file:
    for i, line in enumerate(input_file):
        map_values += [[]]
        map_visited += [[]]

        for value in list(line.strip()):
            map_values[i] += [value]
            map_visited[i] += [False]

MAX_X = len(map_values[0]) - 1
MAX_Y = len(map_values) - 1

def find_similar_neighbours(values: list[list[str]], needle: str, current_position: tuple[int, int]) -> list[tuple[int, int]]:
    similar_neighbours = []

    current_x, current_y = current_position
    for direction in directions_neighbours:
        new_x = current_x+ direction[0]
        new_y = current_y + direction[1]
        if new_x >= 0 and new_x <= MAX_X and new_y >= 0 and new_y <= MAX_Y and values[new_x][new_y] == needle:
            similar_neighbours += [(new_x, new_y)]
    
    return similar_neighbours

def find_region(values: list[list[str]], visited: list[list[bool]], needle: str, current_position: tuple[int, int], found_sofar: list[tuple[tuple[int, int], list[tuple[int, int]]]]) -> None:
    current_x, current_y = current_position
    # print(f"Needle: {needle} current: {values[]}")
    if current_x < 0 or current_x > MAX_X or current_y < 0 or current_y > MAX_Y:
        return []
    if visited[current_x][current_y]:
        return []
    if values[current_x][current_y] != needle:
        return []

    new_point = (current_position, find_similar_neighbours(values, needle, current_position))
    found_sofar += [new_point]
    visited[current_x][current_y] = True

    for direction in directions_neighbours:
        new_position = (current_x + direction[0], current_y + direction[1])
        find_region(values, visited, needle, new_position, found_sofar)

for i, line in enumerate(map_values):
    for j, value in enumerate(line):
        if map_visited[i][j]:
            continue
        new_region = []
        find_region(map_values, map_visited, value, (i, j), new_region)
        regions += [new_region]

solution = 0
for region in regions:
    solution += len(region) * sum(4-len(point[1]) for point in region)

print(solution)