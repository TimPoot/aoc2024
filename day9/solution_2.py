import math
import sys

sys.setrecursionlimit(100000)

BLANK_CHAR = '.'

# (index, size, is_empty)
# disk_files: list[tuple[int, int, bool]] = []
# (index, size, is_empty, is_swapped)
disk_files: list[tuple[int, int, bool, bool]] = []
disk_files_buffer: list[tuple[int, int, bool, bool]] = []

with open('input.txt', 'r') as input_file:
    input_numbers = list(map(int, list(input_file.read().strip()))) 

    for i, number in enumerate(input_numbers):

        disk_files += [(i, number, i % 2 != 0, False)]

def find_swap_index(haystack: list[tuple[int, int, bool, bool]], required_size) -> int:
    haystack.reverse()
    for i, element in enumerate(haystack):
        if not element[2]: 
            continue

        if required_size <= element[1]:
            return i

    return -1

def defrag(unfragmented_list: list[tuple[int, int, bool, bool]]) -> list[tuple[int, int, bool, bool]]:
    if unfragmented_list == []:
        return []
    
    current_file = unfragmented_list[0]
    if current_file[2] or current_file[3]:
        return [unfragmented_list[0]] + defrag(unfragmented_list[1:])
    
    swap_index = find_swap_index(unfragmented_list[1:], current_file[1])
    if swap_index == -1:
        return [unfragmented_list[0]] + defrag(unfragmented_list[1:])
    swap_index = len(unfragmented_list) - find_swap_index(unfragmented_list[1:], current_file[1]) - 1
    
    unfragmented_list[0] = (current_file[0], current_file[1], current_file[2], True)
    current_file = unfragmented_list[0]
    file_to_swap = unfragmented_list[swap_index]
    if current_file[1] == file_to_swap[1]:
        # Same size, swap only
        unfragmented_list[0], unfragmented_list[swap_index] = unfragmented_list[swap_index], unfragmented_list[0]
        return [unfragmented_list[0]] + defrag(unfragmented_list[1:])

    # Size difference, swap n split empty space
    size_difference = file_to_swap[1] - current_file[1]
    unfragmented_list[swap_index] = (-1, current_file[1], True, True)
    unfragmented_list[swap_index] = (-1, current_file[1], True, True)
    unfragmented_list[0], unfragmented_list[swap_index] = unfragmented_list[swap_index], unfragmented_list[0]
    unfragmented_list.insert(swap_index, (-1, size_difference, True, True))
    return [unfragmented_list[0]] + defrag(unfragmented_list[1:])

disk_files.reverse()
disk_files_buffer = defrag(disk_files)

# i = len(disk_files) - 1
# disk_files.reverse()
# disk_files_buffer = disk_files
# for i, file in enumerate(disk_files):
#     current_file = disk_files[i]
#     if current_file[2] or current_file[3]:
#         continue

#     swap_index = find_swap_index(disk_files[i:], current_file[1])
#     if swap_index == -1:
#         continue

#     disk_files[i] = (current_file[0], current_file[1], current_file[2], True)
#     current_file = disk_files[i]
#     file_to_swap = disk_files[swap_index]
#     if file_to_swap[1] == current_file[1]:
#         # Same size, no split necessary
#         disk_files_buffer[i], disk_files_buffer[swap_index] = disk_files_buffer[swap_index], disk_files_buffer[i]
#         continue
    
#     # Different size, split necessary
#     new_empty_space = (-1, file_to_swap[1] - current_file[1], True, False)
#     disk_files_buffer[swap_index] = (file_to_swap[0], current_file[1], True, False)
#     disk_files[i], disk_files[swap_index] = disk_files[swap_index], disk_files[i]
#     disk_files.insert(swap_index + 1, new_empty_space)

disk_files_buffer.reverse()
disk_file_string = ''
for element in disk_files_buffer:
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