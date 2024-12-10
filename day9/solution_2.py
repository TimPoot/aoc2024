import math

BLANK_CHAR = '.'

# (index, size, is_empty)
disk_files: list[tuple[int, int, bool]] = []

with open('input.txt', 'r') as input_file:
    input_numbers = list(map(int, list(input_file.read().strip()))) 

    for i, number in enumerate(input_numbers):

        disk_files += [(i, number, i % 2 != 0)]

def find_swap_index(haystack: list[tuple[int, int, bool]], required_size) -> int:
    for i, element in enumerate(haystack):
        if not element[2]: 
            continue

        if required_size <= element[1]:
            return i

    return -1

i = len(disk_files) - 1
while i > -1:
    current_file = disk_files[i]
    if current_file[2]:
        i -= 1
        continue

    swap_index = find_swap_index(disk_files[:i], current_file[1])
    if swap_index == -1:
        i -= 1
        continue

    file_to_swap = disk_files[swap_index]
    if file_to_swap[1] == current_file[1]:
        disk_files[i], disk_files[swap_index] = disk_files[swap_index], disk_files[i]
        i -= 1
        continue
    
    new_empty_space = (-1, file_to_swap[1] - current_file[1], True)
    disk_files[swap_index] = (file_to_swap[0], current_file[1], True)
    disk_files[i], disk_files[swap_index] = disk_files[swap_index], disk_files[i]
    disk_files.insert(swap_index + 1, new_empty_space)
    i -= 2

disk_file_string = ''
for element in disk_files:
    if element[2]:
        disk_file_string += BLANK_CHAR * element[1]
    else:
        disk_file_string += str(math.floor(element[0] / 2)) * element[1]

checksum = 0
for i, element in enumerate(list(disk_file_string)):
    if element == BLANK_CHAR:
        continue

    checksum += int(element) * i

print(checksum)