import math

BLANK_CHAR = chr(0)

disk: list[str] = []

with open('input.txt', 'r') as input_file:
    input_numbers = list(map(int, list(input_file.read().strip()))) 

    for i, number in enumerate(input_numbers):
        character_to_fill: str = ''
        if i % 2 == 0:
            character_to_fill = chr(math.floor(i / 2) + 1)
        else:
            character_to_fill = BLANK_CHAR

        disk += [character_to_fill for _ in range(number)]

def find_to_fill_index(unsegmented_list: list[str]) -> int:
    for i, current_char in enumerate(unsegmented_list):
        if current_char == BLANK_CHAR and i + 1 < len(unsegmented_list) and any(next_char != BLANK_CHAR for next_char in unsegmented_list[i + 1:]):
            return i
        
    return -1

def find_to_fill_index_file(unsegmented_list: list[str], size_required: int) -> int:
    for i, current_char in enumerate(unsegmented_list):
        if current_char == BLANK_CHAR and i + 1 < len(unsegmented_list) and any(next_char != BLANK_CHAR for next_char in unsegmented_list[i + 1:]):
            if size_required == 1:
                return i

            slot_size = 1
            for j in range(len(unsegmented_list[i + 1:])):
                if unsegmented_list[i + j + 1] != BLANK_CHAR:
                    break

                slot_size += 1
                if slot_size == size_required:
                    return i
        
    return -1

# Segment disk per byte
# for i in range(len(disk) - 1, -1, -1):
#     index_to_fill = find_to_fill_index(disk)
#     if index_to_fill == -1:
#         break
#     else:
#         disk[i], disk[index_to_fill] = disk[index_to_fill], disk[i]

# Segment disk per file
i = len(disk) - 1
while i > 0:
    if disk[i] == BLANK_CHAR:
        i = i - 1
        continue

    file_end = i
    file_begin = disk.index(disk[i])
    size_required = (file_end - file_begin) + 1

    swap_begin = find_to_fill_index_file(disk[:file_begin], size_required)
    if swap_begin != -1:
        for j in range(size_required):
            disk[swap_begin + j], disk[file_begin + j] = disk[file_begin + j], disk[swap_begin + j]

    i = file_begin - 1

checksum = 0
for i, number in enumerate(disk):
    if number == BLANK_CHAR:
        continue

    checksum += (ord(number) - 1) * i

print(checksum)