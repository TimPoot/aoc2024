

directions_dict: dict[str, tuple[int, int]] = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}
fish_map: list[list[str]] = []
current_pos = (-1, -1)

def tuple_addition(t1, t2):
    if len(t1) != len(t2):
        print("Len tuples not the same")
        return -1

    new_tuple = []
    for i in range(len(t1)):
        new_tuple.append(t1[i] + t2[i])

    return tuple(new_tuple)

def get_value_at_tuple(list_2d, t):
    return list_2d[t[0]][t[1]]

def set_value_at_tuple(list_2d, t, val):
    list_2d[t[0]][t[1]] = val

def print_2d_array(list_2d):
    for x in list_2d:
        for y in x:
            print(y, end="")
        print("")


with open("input.txt", "r") as input_file:
    for line in input_file:
        stripped_line = line.strip()

        if "#" in line or "." in line or "O" in line:
            fish_map += [[]]
            for point in stripped_line:
                fish_map[-1] += point
                if point == "@":
                    current_pos = (len(fish_map[-1]) - 1, len(fish_map) - 1)

        elif ">" in line or "<" in line or "^" in line or "v" in line:

            for step in stripped_line:
                encountered_box_positions = []
                current_direction = directions_dict[step]

                pos_to_check = tuple_addition(current_pos, current_direction)
                while get_value_at_tuple(fish_map, pos_to_check) == "O":
                    encountered_box_positions.append(pos_to_check)
                    pos_to_check = tuple_addition(pos_to_check, current_direction)

                # No free space, do nothing
                if get_value_at_tuple(fish_map, pos_to_check) == "#":
                    continue
                
                new_pos = tuple_addition(current_pos, current_direction)
                set_value_at_tuple(fish_map, current_pos, ".")
                set_value_at_tuple(fish_map, new_pos, "@")
                current_pos = new_pos

                if len(encountered_box_positions) > 0:
                    set_value_at_tuple(fish_map, pos_to_check, "O")

gps_score = 0
for i, line in enumerate(fish_map):
    for j, point in enumerate(line):
        if point == "O":
            gps_score += 100 * i + j

print(gps_score)