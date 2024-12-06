import re
import math

regex1 = r'mul\((\d{1,3}),(\d{1,3})\)'
regex2 = r'(do\(\)|don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)'

def part1(input_string):
    total = 0
    matched_pairs = re.findall(regex1, input_string)

    for pair in matched_pairs:
        total += math.prod(list(map(int, pair)))

    print(total)
    
def part2(input_string):
    total = 0
    do = 'do()'
    dont = 'don\'t()'
    matched_pairs = re.findall(regex2, input_string)

    is_enabled = True
    for pair in matched_pairs:
        if pair[0] == do:
            is_enabled = True
            continue
        if pair[0] == dont:
            is_enabled = False
        if is_enabled and pair[0] == '':
            total += int(pair[1]) * int(pair[2])

    print(total)

with open('input.txt', 'r') as input_file:
    input_string = ''.join(input_file)
    part2(input_string)