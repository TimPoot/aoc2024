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

    for i in range(len(pages)):
        if pages[i] in rule_dict:
            if any(page_found in rule_dict[pages[i]] for page_found in pages_so_far):
                # Logic here
                new_index: int = 0
                for j in range(1, i+1):
                    page_being_checked = pages[i-j]
                    if page_being_checked in rule_dict and pages[i] in rule_dict[page_being_checked]:
                        new_index = i-j+1
                        break

                pages[i], pages[new_index] = pages[new_index], pages[i]
                if is_instruction_good(pages):
                    return pages
                pages_so_far = []
                i = 0

        pages_so_far += [pages[i]]

    return fix_instruction(pages)

good_sum = 0
with open('input.txt', 'r') as input_file:
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