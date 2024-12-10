directions: list[tuple[int, int]] = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

mountain_map: list[list[int]] = []

with open("input.txt", 'r') as input_file:
    for i, line in enumerate(input_file):
        mountain_map += [[]]
        
        for number in list(line):
            if number == '\n':
                continue
            mountain_map[i] += [int(number.strip())]

max_x = len(mountain_map[0]) - 1
max_y = len(mountain_map) - 1 

def print_map():
    for line in mountain_map:
        for point in line:
            print(point, end='')
        print()

def find_summits(heigt_required: int, location: tuple[int, int], summits_found: set[tuple[int, int]], part2: bool) -> int:
    if location[0] < 0 or location[0] > max_x or location[1] < 0 or location[1] > max_y:
        return 0

    new_step_value = mountain_map[location[0]][location[1]]
    if new_step_value == heigt_required:
        if new_step_value == 9 and (part2 or not (location in summits_found)):
            summits_found.add(location)
            return 1
        else:
            new_locations = [(location[0] + direction[0], location[1] + direction[1]) for direction in directions]
            return sum(find_summits(heigt_required + 1, new_location, summits_found, part2) for new_location in new_locations) 
                
    return 0

trailhead_sum = 0
for i, line in enumerate(mountain_map):
    for j, point in enumerate(line):
        if point == 0:
            trailhead_sum += find_summits(0, (i, j), set(), True)


print(trailhead_sum)