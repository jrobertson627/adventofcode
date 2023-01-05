'''
    Programmer: Jessica Robertson
    Date Written: 12-2-2022

    Problem Link: adventofcode.com/2022/day2
    Sources Used:

    Script File for day 2 of 2022
'''

import csv

def read_input(filename):
    '''
    Read puzzle input to create a strategy guide

    Args:
        filename(string): The path to the puzzle input
    Returns:
        given_moves(List of Str): The strategy guide to follow in list format
            Index 0 refers to the opponents move
            Index 1 refers to your move
    '''
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        given_moves = []
        for row in csv_reader:
            new_row = []
            for col in row:
                new_row.append(col)
            given_moves.append(new_row)

    return given_moves

def transform_pt1(play_list):
    '''
    Transform strategy guide into a list of ints corresponding to moves
    Rock: A, X -> 1
    Paper: B, Y -> 2
    Scissors: C, Z -> 3

    Args:
        play_list(List of Str): The strategy guide to follow in list format
            Index 0 refers to the opponents move
            Index 1 refers to your move
    Returns:
        new_list(List of Int): The strategy guide to follow in list format
            Index 0 refers to the opponents move
            Index 1 refers to your move
    '''
    new_list = []
    for row in play_list:
        new_row = []
        for col in row:
            if col in ['A', 'X']:
                new_row.append(1)
            elif col in ['B', 'Y']:
                new_row.append(2)
            else:
                new_row.append(3)
        new_list.append(new_row)
    return new_list

def transform_pt2(play_list):
    '''
    Transform strategy guide into a list of ints corresponding to moves
    Rock: A-> 1, Paper: B -> 2, Scissors: C -> 3
    My Moves: Y -> Draw, X -> Lose, Z -> Win

    Args:
        play_list(List of Str): The strategy guide to follow in list format
            Index 0 refers to the opponents move
            Index 1 refers to your move
    Returns:
        new_list(List of Int): The strategy guide to follow in list format
            Index 0 refers to the opponents move
            Index 1 refers to your move
    '''
    new_list = []
    for row in play_list:
        if row[0] == 'A':
            their_play = 1
        elif row[0] == 'B':
            their_play = 2
        else:
            their_play = 3

        # check if draw
        if row[1] == 'Y':
            my_play = their_play
        # check if lose
        elif row[1] == 'X':
            if their_play == 1:
                my_play = 3
            elif their_play == 2:
                my_play = 1
            else:
                my_play = 2
        # check if win
        else:
            if their_play == 1:
                my_play = 2
            elif their_play == 2:
                my_play = 3
            else:
                my_play = 1
        new_list.append([their_play, my_play])

    return new_list

def get_points(int_list):
    '''
    Use the strategy guide transformed into integers to determine how many points you have

    Args:
        int_list(List of Int): The strategy guide to follow in list format
            Index 0 refers to the opponents move
            Index 1 refers to your move
    Returns:
        points(List of Int): How many points you have per round
    '''
    points = []
    for row in int_list:
        # check if a draw
        if row[0] == row[1]:
            points.append(row[1] + 3)
        # if they choose rock
        elif row[0] == 1:
            if row[1] == 2:
                points.append(row[1] + 6)
            else:
                points.append(row[1] + 0)
        # if they chose paper
        elif row[0] == 2:
            if row[1] == 1:
                points.append(row[1] + 0)
            else:
                points.append(row[1] + 6)
        # if they chose scissors
        else:
            if row[1] == 1:
                points.append(row[1] + 6)
            else:
                points.append(row[1] + 0)
    return points

def get_total(points):
    '''
    Sum the list of points

    Args:
        points(List of Int): How many points you have per round
    Returns:
        sum of points(Int): How many total points you have
    '''
    return sum(points)
