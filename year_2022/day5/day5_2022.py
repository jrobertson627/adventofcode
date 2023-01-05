import csv
import re

def read_input(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        cargo_config = [
            ['W', 'D', 'G', 'B', 'H', 'R', 'V'], # row 1
            ['J', 'N', 'G', 'C', 'R', 'F'], # row 2
            ['L', 'S', 'F', 'H', 'D', 'N', 'J'], # row 3
            ['J', 'D', 'S', 'V'], # row 4
            ['S','H','D','R','Q','W','N','V'], # row 5
            ['P','G','H','C','M'], # row 6
            ['F','J','B','G','L','Z','H','C'], # row 7
            ['S','J','R'], # row 8
            ['L','G','S','R','B','N','V','M']] # row 9
        
        all_instructions = []
        for idx, row in enumerate(csv_reader): 
            if idx > 9:
                curr_row = row[0]
                instruction = list(map(int, re.findall(r'\d+', curr_row)))
                all_instructions.append(instruction)
                
    return cargo_config, all_instructions

def move_single_crate(curr_cargo, num_moved, origin_stack, new_stack):
    for _ in range(num_moved):
        moved_crate = curr_cargo[origin_stack-1].pop(-1)
        curr_cargo[new_stack-1].append(moved_crate)
    return curr_cargo

def move_multiple_crates(curr_cargo, num_moved, origin_stack, new_stack):
    crate_stack = []
    for _ in range(num_moved):
        curr_crate = curr_cargo[origin_stack-1].pop(-1)
        crate_stack.append(curr_crate)
    print(crate_stack)
    for _ in range(len(crate_stack)):
        crate = crate_stack.pop(-1)
        curr_cargo[new_stack-1].append(crate)
    return curr_cargo

def all_movements(curr_cargo, instructions, part):
    if part == 1:
        for row in instructions:
            curr_cargo = move_single_crate(curr_cargo, row[0], row[1], row[2])
    else:
        for row in instructions:
            print(row)
            print("BEGIN")
            print(curr_cargo)
            curr_cargo = move_multiple_crates(curr_cargo, row[0], row[1], row[2])
            print("END")
            print(curr_cargo)
    return curr_cargo

def determine_top(curr_cargo):
    top_of_stack = ''
    for row in curr_cargo:
        curr_top = row[-1]
        top_of_stack+= curr_top
    return top_of_stack

def main():
    cargo, instruction = read_input("input.txt")
    CARGO_BEGIN = [['z', 'n'], ['m', 'c', 'd'], ['p']]
    CARGO_INSTRUCTIONS = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]] # num, origin stack, end stack
    CARGO_END = [['c'], ['m'], ['z', 'n', 'd', 'p']]
    CARGO_TOPS = 'cmz'

    mycargo = all_movements(cargo, instruction, 2)
    new_top = determine_top(mycargo)
    print(new_top)

if __name__ == "__main__":
    main()