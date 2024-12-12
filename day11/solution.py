from functools import lru_cache
from collections import defaultdict
# 0 -> 1 If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# len(x) % 2 == 0 -> split into two, no leading zeros. e.g.: 1000 -> 10 0 If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# else -> n * 2024

number_count_dict: dict[str, int] = defaultdict()

number_list_original: list[str] = []
number_list_new: list[str] = []
N = 75

number_list_original = open('input.txt', 'r').read().strip().split(' ')
number_list_new = number_list_original
number_count_dict = {number: 1 for number in number_list_original}

@lru_cache(maxsize=None)
def transform_number(number: str) -> list[str]:
    if number == '0':
        return ['1']
    elif len(number) % 2 == 0:
        new_number1, new_number2 = int(number[len(number) // 2]), int(number[len(number) // 2:])
        return [str(new_number1), str(new_number2)]
    else:
        return [str(int(number) * 2024)]

def transform_step(number_dict: dict[str, int]) -> dict[str, int]:
    new_stones = defaultdict(int)    
    for number, count in number_dict.items():
        if number == '0':
            new_stones[str(1)] += count
        elif len(number) % 2 == 0:
            new_number1, new_number2 = int(number[:len(number) // 2]), int(number[len(number) // 2:])
            new_stones[str(new_number1)] += count
            new_stones[str(new_number2)] += count
        else:
            new_stones[str(int(number) * 2024)] += count
    
    return new_stones

for i in range(N):
    number_count_dict = transform_step(number_count_dict)

# print(number_list_new)
print(sum(number_count_dict.values()))