'''
    Programmer: Jessica Robertson
    Date Written: 12-1-2022

    Problem Link: adventofcode.com/2022/day1
    Sources Used:

    Test file for day 1 of 2022
'''

import day1_2022 as day1
import numpy as np

TEST_ARRAY = [6000, 4000, 11000, 24000, 10000]
TEST_TOP_CAL = 24000
TEST_TOP_THREE_CAL = 45000

def test_find_top_num():
    _, top_num = day1.find_most_cal(TEST_ARRAY)
    assert top_num == TEST_TOP_CAL

def test_find_top_three():
    top_three = day1.find_top_three(TEST_ARRAY)
    assert top_three == TEST_TOP_THREE_CAL
