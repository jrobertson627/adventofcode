'''
    Programmer: Jessica Robertson
    Date Written: 12-5-2022

    Problem Link: adventofcode.com/2022/day5
    Sources Used:

    Script File for day 5 of 2022
'''

import csv
import re

def read_input(filename):
    '''
    Read puzzle input to determine instructions and the current stacks

    Args:
        filename(string): The path to the puzzle input
    Returns:
        cargo_config(List of list of str): Each puzzle stack where
            each row corresponds to a single stack with [-1] being the
            top of the stack
        all_instructions(List of list of ints): The instructions to move
        the stacks where each row corresponds to a single instruction list
        [number to move, where to take the boxes from, where to put the boxes]
    '''
    with open(filename, encoding="utf-8") as csv_file:
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
    '''
    Using the provided arguments, move the crates one by one to their
    new location

    Args:
        curr_cargo(List of list of str): The current stack configuration
        num_moved(int): How many boxes to move
        origin_stack(int): The corresponding row-1 in curr_cargo to
            move the boxes from
        new_stack(int): The corresponding row-1 in curr_cargo to set the boxes
    Returns:
        curr_cargo(List of list of str): The new stack configuration
    '''
    for _ in range(num_moved):
        moved_crate = curr_cargo[origin_stack-1].pop(-1)
        curr_cargo[new_stack-1].append(moved_crate)
    return curr_cargo

def move_multiple_crates(curr_cargo, num_moved, origin_stack, new_stack):
    '''
    Using the provided arguments, move the crates all at once to their
    new location

    Args:
        curr_cargo(List of list of str): The current stack configuration
        num_moved(int): How many boxes to move
        origin_stack(int): The corresponding row-1 in curr_cargo to
            move the boxes from
        new_stack(int): The corresponding row-1 in curr_cargo to set the boxes
    Returns:
        curr_cargo(List of list of str): The new stack configuration
    '''
    crate_stack = []
    for _ in range(num_moved):
        curr_crate = curr_cargo[origin_stack-1].pop(-1)
        crate_stack.append(curr_crate)
    for _ in range(len(crate_stack)):
        crate = crate_stack.pop(-1)
        curr_cargo[new_stack-1].append(crate)
    return curr_cargo

def all_movements(curr_cargo, instructions, part):
    '''
    Using the provided arguments, move the crates one by one to their
    new location

    Args:
        curr_cargo(List of list of str): The current stack configuration
        instructions(List of list of int): All instructions from puzzle input
        part(int): Is part 1 being executed or part 2
    Returns:
        curr_cargo(List of list of str): The new stack configuration
    '''
    if part == 1:
        for row in instructions:
            curr_cargo = move_single_crate(curr_cargo, row[0], row[1], row[2])
    else:
        for row in instructions:
            curr_cargo = move_multiple_crates(curr_cargo, row[0], row[1], row[2])
    return curr_cargo

def determine_top(curr_cargo):
    '''
    Determine the top of each stack

    Args:
        curr_cargo(List of list of str): The current stack configuration
    Returns:
        top_of_stack(str): Each box at the top
    '''
    top_of_stack = ''
    for row in curr_cargo:
        curr_top = row[-1]
        top_of_stack+= curr_top
    return top_of_stack
