rule_dict: dict[int, list[int]] = dict()

def set_rule(line: str) -> None:
    key, value = list(map(int, line.split('|')))
    if key in rule_dict:
        rule_dict[key] += [value]
    else:
        rule_dict[key] = [value]

def is_instruction_good(pages: list[int]) -> bool:
    pages_so_far: list[int] = []

    for page in pages:
        if page in rule_dict:
            if any(page_found in rule_dict[page] for page_found in pages_so_far):
                return False

        pages_so_far += [page]

    return True
            
def fix_instruction(pages: list[int]) -> list[int]:
    pages_so_far: list[int] = []
    altered_instruction: list[int] = []

    for i, page in enumerate(pages):
        if page in rule_dict:
            if any(page_found in rule_dict[page] for page_found in pages_so_far):
                # Logic here
                altered_instruction = pages
                for j in range(1, i+1):
                    altered_instruction[i-j], altered_instruction[i] = altered_instruction[i], altered_instruction[i-j]
                    if is_instruction_good(altered_instruction):
                        print('~~ HELLO ~~')
                        print(page)
                        return altered_instruction

        pages_so_far += [page]

    print(altered_instruction)
    return []

good_sum = 0
with open('input_example.txt', 'r') as input_file:
    set_rules = True
    for line in input_file:
        if line == '\n':
            set_rules = False
            continue

        if set_rules:
            set_rule(line)
        else:
            pages = list(map(int, line.split(',')))
            # Part 1
            # if is_instruction_good(pages):
            #     good_sum += pages[int(len(pages)/2)]

            # Part 2
            if not is_instruction_good(pages):
                fixed_instruction: list[int] = fix_instruction(pages)
                if fixed_instruction == []:
                    print('Something very weird has happened')

                good_sum += fixed_instruction[int(len(fixed_instruction)/2)]

print(good_sum)