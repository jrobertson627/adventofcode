import os
import day1_2015 as day1
import numpy as np

#Test for Part 1
TEST_INPUT_1 = "(())"
TEST_RESULT_1 = 0

TEST_INPUT_2 = "()()"
TEST_RESULT_2 = 0

TEST_INPUT_3 = "((("
TEST_RESULT_3 = 3

TEST_INPUT_4 = "(()(()("
TEST_RESULT_4 = 3

TEST_INPUT_5 = "))((((("
TEST_RESULT_5 = 3

TEST_INPUT_6 = "())"
TEST_RESULT_6 = -1

TEST_INPUT_7 = "))("
TEST_RESULT_7 = -1

TEST_INPUT_8 = ")))"
TEST_RESULT_8 = -3

TEST_INPUT_9 = ")())())"
TEST_RESULT_9 = -3

#Tests for Part 2
TEST_INPUT_10 = ")"
TEST_RESULT_10 = 1

TEST_INPUT_11 = "()())"
TEST_RESULT_11 = 5

#Check the floor based on full input
def test_change_floor_1():
    floor = 0
    counter = 0
    TEST_ARRAY_1 = list(TEST_INPUT_1)
    for character in TEST_ARRAY_1:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_1)

def test_change_floor_2():
    floor = 0
    counter = 0
    TEST_ARRAY_2 = list(TEST_INPUT_2)
    for character in TEST_ARRAY_2:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_2)

def test_change_floor_3():
    floor = 0
    counter = 0
    TEST_ARRAY_3 = list(TEST_INPUT_3)
    for character in TEST_ARRAY_3:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_3)

def test_change_floor_4():
    floor = 0
    counter = 0
    TEST_ARRAY_4 = list(TEST_INPUT_4)
    for character in TEST_ARRAY_4:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_4)

def test_change_floor_5():
    floor = 0
    counter = 0
    TEST_ARRAY_5 = list(TEST_INPUT_5)
    for character in TEST_ARRAY_5:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_5)

def test_change_floor_6():
    floor = 0
    counter = 0
    TEST_ARRAY_6 = list(TEST_INPUT_6)
    for character in TEST_ARRAY_6:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_6)

def test_change_floor_7():
    floor = 0
    counter = 0
    TEST_ARRAY_7 = list(TEST_INPUT_7)
    for character in TEST_ARRAY_7:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_7)

def test_change_floor_8():
    floor = 0
    counter = 0
    TEST_ARRAY_8 = list(TEST_INPUT_8)
    for character in TEST_ARRAY_8:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_8)

def test_change_floor_9():
    floor = 0
    counter = 0
    TEST_ARRAY_9 = list(TEST_INPUT_9)
    for character in TEST_ARRAY_9:
        floor, counter = day1.change_floor(floor, character, counter)
    assert(floor, TEST_RESULT_9)

#Check what position in the array the floor is -1
def test_check_floor_1():
    floor = 0
    counter = 0
    TEST_ARRAY_10 = list(TEST_INPUT_10)
    for character in TEST_ARRAY_10:
        floor, counter = day1.change_floor(floor, character, counter)
        pos_check = day1.check_floor(floor)
        if pos_check == True:
            break
    assert(counter, TEST_RESULT_10)

def test_check_floor_2():
    floor = 0
    counter = 0
    TEST_ARRAY_11 = list(TEST_INPUT_11)
    for character in TEST_ARRAY_11:
        floor, counter = day1.change_floor(floor, character, counter)
        pos_check = day1.check_floor(floor)
        if pos_check == True:
            break
    assert(counter, TEST_RESULT_11)