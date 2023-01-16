'''
    Programmer: Jessica Robertson
    Date Written: 1-11-2023

    Problem Link: adventofcode.com/2022/day3
    Sources Used:

    Script File for day 3 of 2022
'''

import csv

def read_input(filename):
    '''
    Read puzzle input to determine which sacks have
        been packed wrong

    Args:
        filename(string): The path to the puzzle input
    Returns:
        all_sacks(List of strings): Each sack's items
    '''
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        all_sacks = []
        for row in csv_reader:
            all_sacks.append(row)
    return all_sacks

def split_sacks(all_sacks):
    '''
    Split each row into 2 equal length strings

    Args:
        all_sacks(List of strings): Each sack's items
    Returns:
        split_sacks(List of strings): Each sack's items where
        split_sacks[0] refers to the first string
        split_sacks[1] refers to the second string
    '''

    edited_stacks = []
    for _, bag in enumerate(all_sacks):
        curr_string = bag[0]
        len_string = len(curr_string)
        if len_string%2 == 0:
            slice_sub1 = slice(0, len_string//2)
            slice_sub2 = slice(len_string//2, len_string)
            string1 = curr_string[slice_sub1]
            string2 = curr_string[slice_sub2]
            new_split = []
            new_split.append(string1)
            new_split.append(string2)
            edited_stacks.append(new_split)
    return edited_stacks

def find_duplicates(compartment1, compartment2):
    '''
    Given 2 equal length strings find if there are
        any duplicate chars between the strings

    Args:
        compartment1(str): The first part of the bag
        compartment2(str): The second part of the bag
    Returns:
        duplicate_item(List of str): Items in both compartments
    '''
    duplicates = []
    for char in compartment1:
        if char in compartment2:
            if char not in duplicates:
                duplicates.append(char)
    return duplicates

def determine_priority(duplicates):
    '''
    Given a list of duplicate chars, assign a priority int

    Args:
        duplicates(List of char): Each duplicated item
    Returns:
        duplicates_int(List of ints): A priority int for each duplicated item
    '''
    duplicates_int = []
    for row in duplicates:
        for col in row:
            acs_val = ord(col)
            if acs_val < 91:
                priority = acs_val - 38
            else:
                priority = acs_val - 96
            duplicates_int.append(priority)
    return duplicates_int

def find_badges(all_sacks):
    '''
    For every 3 lines (a single group) determine the common item

    Args:
        all_sacks(List of strings): Each sack's items
    Returns:
        badges(List of str): Each badge per group
    '''
    badges = []
    while all_sacks:
        member1 = all_sacks.pop(0)
        member2 = all_sacks.pop(0)
        member3 = all_sacks.pop(0)
        for char in member1[0]:
            if char in member2[0]:
                if char in member3[0]:
                    badges.append(char)
                    break

    return badges

def complete_part1(rucksacks):
    '''
    Execute part 1

    Args:
        rucksacks(List of strings): Each sack's items
    Returns:
        sum_priority(int): The sum of each item's priority
    '''
    splits = split_sacks(rucksacks)
    duplicates = []
    for row in splits:
        duplicates.append(find_duplicates(row[0], row[1]))
    priorities = determine_priority(duplicates)
    sum_priority = sum(priorities)
    return sum_priority

def complete_part2(rucksacks):
    '''
    Execute part 2

    Args:
        rucksacks(List of strings): Each sack's items
    Returns:
        sum_badges(int): The sum of each groups priority
    '''
    badges = find_badges(rucksacks)
    badge_priority = determine_priority(badges)
    sum_badges = sum(badge_priority)
    return sum_badges
