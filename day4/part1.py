
NEEDLE = list('XMAS')
DIRECTIONS = [
    (-1,-1),
    (0,-1),
    (1,-1),
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
    (-1,0)
]
DIAGONAL_1 = [
    (1,-1),
    (-1,1),
]
DIAGONAL_2 = [
    (-1,-1),
    (1,1),
]

def is_oob(haystack: list[list[str]], coord: tuple[int, int]):
    x, y = coord
    if x >= len(haystack) or x < 0 or y >= len(haystack[x]) or y < 0:
        return True
    
    return False

def take_step(haystack: list[list[str]], current_coords: tuple[int, int], 
              direction: tuple[int, int], step_counter: int) -> bool:
    
    new_x = current_coords[0] + direction[0]
    new_y = current_coords[1] + direction[1]
    # Step goes out of bounds -> False
    if is_oob(haystack, (new_x, new_y)):
        return False

    step_value = haystack[new_x][new_y]
    # Step does not result in needed value -> False
    if step_value != NEEDLE[step_counter]:
        return False
    
    if step_counter == 3:
        return True
    
    return take_step(haystack, (new_x, new_y), direction, step_counter + 1)

def check_diagonals(haystack: list[list[str]], current_coords: tuple[int, int]) -> bool:
    prev = 'Z'
    for diagonal in DIAGONAL_1:
        new_x = current_coords[0] + diagonal[0] 
        new_y = current_coords[1] + diagonal[1] 
        if is_oob(haystack, (new_x, new_y)) or haystack[new_x][new_y] == 'X' or haystack[new_x][new_y] == 'A' or haystack[new_x][new_y] == prev:
            return False

        prev = haystack[new_x][new_y]

    prev = 'Z'
    for diagonal in DIAGONAL_2:
        new_x = current_coords[0] + diagonal[0] 
        new_y = current_coords[1] + diagonal[1] 
        if is_oob(haystack, (new_x, new_y)) or haystack[new_x][new_y] == 'X' or haystack[new_x][new_y] == 'A' or haystack[new_x][new_y] == prev:
            return False

        prev = haystack[new_x][new_y]

    return True

counter = 0
with open('input.txt', 'r') as input_file:
    haystack = list(map(list, input_file.read().splitlines()))

    for i in range(0, len(haystack)):
        for j in range(0, len(haystack[0])):

            # Part 1
            # if haystack[i][j] == NEEDLE[0]:
            #     for direction in DIRECTIONS:
            #         if take_step(haystack, (i, j), direction, 1):
            #             counter += 1

            # Part 2
            if haystack[i][j] == NEEDLE[2]:
                if check_diagonals(haystack, (i, j)):
                    counter += 1

print(counter)