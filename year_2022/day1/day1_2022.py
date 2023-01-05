'''
    Programmer: Jessica Robertson
    Date Written: 12-1-2022

    Problem Link: adventofcode.com/2022/day1
    Sources Used:

    Script File for day 1 of 2022
'''
import csv

def read_input(filename):
    '''
    Read puzzle input and then create a list of
        how many calories each elf has

    Args:
        filename(string): The path to the puzzle input
    Returns:
        tot_cal_per_elf(List): How many calories each elf has
    '''
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        tot_cal_per_elf = []
        curr_cal = 0
        for row in csv_reader:
            if not row:
                tot_cal_per_elf.append(curr_cal)
                curr_cal = 0
            else:
                num = int(row[0])
                curr_cal += num
    tot_cal_per_elf.append(curr_cal)
    return tot_cal_per_elf

def find_most_cal(elf_list):
    '''
    Find the most calories within the list of all calories per elf

    Args:
        elf_list(List): How many calories each elf has
    Returns:
        elf_index(int): Which elf has the most calories
        elf_cals(int): How many calories the elf has
    '''
    elf_cals = max(elf_list)
    elf_index = elf_list.index(elf_cals)
    return elf_index, elf_cals

def find_top_three(elf_list):
    '''
    Find how many calories the top three elves have

    Args:
        elf_list(List): How many calories each elf has
    Returns:
        total_cals(int): The sum of the top three calories found
    '''
    total_cals = 0
    for _ in range(3):
        elf_index, elf_cals = find_most_cal(elf_list)
        elf_list.pop(elf_index)
        total_cals += elf_cals
    return total_cals
