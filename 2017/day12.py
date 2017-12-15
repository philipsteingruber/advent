import re
from collections import OrderedDict

def main():
    with open('input.txt') as file:
        lines = file.readlines()

    pattern = re.compile(r'(\w+) <-> ([\d, ]+)')

    programs_dict = OrderedDict()
    groups = []

    for line in lines:
        program, connected_programs = re.match(pattern, line).groups()
        programs_dict[int(program)] = list(map(int, connected_programs.split(', ')))

    connected_to_zero_list = []
    for program, connected_programs in programs_dict.items():
        in_group_zero, visited_programs = connected_to_zero(program, programs_dict, [])
        if in_group_zero:
            connected_to_zero_list.append(program)
        visited_programs.sort()
        if visited_programs not in groups:
            groups.append(visited_programs)

    groups = sorted(groups, key=len, reverse=True)
    groups = fix_groups(groups)


    print('Step 1 solution:', len(connected_to_zero_list))
    print('Step 2 solution:', len(groups))

def fix_groups(groups):
    fixed_groups = []
    for group in groups:
        new_group_found = True
        for program in group:
            for fixed_group in fixed_groups:
                if program in fixed_group:
                    new_group_found = False
        if new_group_found:
            fixed_groups.append(group)
    return fixed_groups

def connected_to_zero(program, programs_dict, visited_programs):
    visited_programs.append(program)
    if program == 0:
        return True, visited_programs
    elif 0 in programs_dict[program]:
        visited_programs.append(0)
        return True, visited_programs
    for connected_program in programs_dict[program]:
        if connected_program not in visited_programs:
            in_group_zero, visited_programs = connected_to_zero(connected_program, programs_dict, visited_programs)
            if in_group_zero:
                return True, visited_programs
    return False, visited_programs

if __name__ == '__main__':
    main()
