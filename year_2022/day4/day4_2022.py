'''
    Programmer: Jessica Robertson
    Date Written: 1-11-2023

    Problem Link: adventofcode.com/2022/day4
    Sources Used:

    Script File for day 4 of 2022
'''

import csv

def read_input(filename):
    '''
    Read puzzle input to determine which sacks have
        been packed wrong

    Args:
        filename(string): The path to the puzzle input
    Returns:
        cleaning_sections(List of int): A list of cleaning partners
    '''
    cleaning_sections = []
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        for row in csv_reader:
            cleaning_sections.extend(row)
            
    cleaning_ints = prepare_data(cleaning_sections)
    return cleaning_ints

def prepare_data(cleaning_sections):
    '''
    Convert the list to be integers

    Args:
        cleaning_sections(List of str): The original list
    Returns:
        new_cleaner(List of int): A list of cleaning partners
    '''
    new_cleaner = []
    for row in cleaning_sections:
        if len(row) == 4:
            new_row = []
            first_pair, second_pair = [list(map(int, pair.split('-'))) for pair in row.split(",")]
            new_row.extend(first_pair)
            new_row.extend(second_pair)
            new_cleaner.append(new_row)
    return new_cleaner        
    
def determine_full_overlap(cleaning_sections):
    '''
    Determine which pairs fully overlap

    Args:
        cleaning_sections(List of int): A list of cleaning partners
    Returns:
        num_full_overlap(int): How many partners fully overlap
    '''
    num_full_overlap = 0
    
    for row in cleaning_sections:
        one_cleaner = [row[0], row[1]]
        two_cleaner = [row[2], row[3]]
    # determine if one range if completely in the other
        
    # do the two elves start at the same spot
        if one_cleaner[0] != two_cleaner[0]:
            if one_cleaner[0] > two_cleaner[0]:
                inside_range, outside_range = one_cleaner, two_cleaner
                # print("One", one_cleaner, two_cleaner)
            else:
                inside_range, outside_range = two_cleaner, one_cleaner
                # print("Two", one_cleaner, two_cleaner)
        else: # yes they start at the same spot
            # does the second elf clean for longer
            if one_cleaner[1] < two_cleaner[1]:
                inside_range, outside_range = one_cleaner, two_cleaner
                # print("Three", one_cleaner, two_cleaner)
            # the first elf cleans for longer
            else:
                inside_range, outside_range = two_cleaner, one_cleaner
                # print("Four", one_cleaner, two_cleaner)
        if inside_range[1] <= outside_range[1]:
            num_full_overlap += 1

    return num_full_overlap

def determine_any_overlap(cleaning_sections):
    '''
    Determine which pairs partially overlap

    Args:
        cleaning_sections(List of int): A list of cleaning partners
    Returns:
        overlap(int): How many partners partially overlap
    '''
    overlap = 0
    no_overlap = 0
    for row in cleaning_sections:
        one_cleaner = [row[0], row[1]]
        two_cleaner = [row[2], row[3]]
        
        if one_cleaner[0] != two_cleaner[0]:
            # they don't start at the same spot
            if one_cleaner[1] < two_cleaner[0]:
                # first elf stops before second elf starts
                no_overlap += 1
                # print("One", one_cleaner, two_cleaner)
            elif two_cleaner[1] < one_cleaner[0]:
                # second elf stops before first elf starts
                no_overlap += 1
                # print("Two", one_cleaner, two_cleaner)
            else:
                overlap += 1
                # print("Three", one_cleaner, two_cleaner)
        else:
            overlap += 1
            # print("Four", one_cleaner, two_cleaner)
    return overlap
