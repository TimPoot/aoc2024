import numpy as np

def add(a: int, b: int) -> int:
    return a + b


def mult(a: int, b: int) -> int:
    return a * b

def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))

possible_functions = [add, mult]

possible_functions_2 = [add, mult, concat]

good_sum = 0
with open('input.txt', 'r') as input_file:
    for line in input_file:
        numbers = line.split(' ')
        solution = int(numbers[0][:-1])
        parts = [int(number.strip()) for number in numbers[1:]]
        amount_functions_required = len(parts)-1

        # Part 1
        # for i in range(pow(2, amount_functions_required)):
        #     function_permutation_bins = list(map(int, list(format(i, f'0{amount_functions_required}b'))))

        #     current_result = parts[0]
        #     for j in range(amount_functions_required):
        #         current_result = possible_functions[function_permutation_bins[j]](current_result, parts[j + 1])
                
        #     if current_result == solution:
        #         good_sum += solution
        #         break

        # Part 2
        for i in range(pow(3, amount_functions_required)):
            function_permutation_bins = list(map(int, list(np.base_repr(i, base=3).zfill(amount_functions_required))))

            current_result = parts[0]
            for j in range(amount_functions_required):
                current_result = possible_functions_2[function_permutation_bins[j]](current_result, parts[j + 1])
                
            if current_result == solution:
                good_sum += solution
                break

print(good_sum)