from pickle import FALSE
import day2
import numpy as np
import os

TEST_ARRAY = np.array([("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)])
TEST_BREAK_STRING = "forward 5"
TEST_BREAK_STRING_RESULT = [("forward", 5)]
TEST_RESULT_HORIZ_POS = 15
TEST_RESULT_SIMPLE_DEPTH = 10
TEST_RESULT_SIMPLE_FINAL_POS = 150
TEST_RESULT_DEPTH = 60
TEST_RESULT_FINAL_POS = 900

def test_changeDepth():
    newdepth = day2.changeDepth(0, -5)
    assert newdepth == -5

def test_changePos():
    newpos = day2.changePos(0, 5)
    assert newpos == 5

def test_split():
    value = day2.text_num_split(TEST_BREAK_STRING)
    np.testing.assert_array_almost_equal(value, TEST_BREAK_STRING_RESULT)

def test_input():
    os.chdir(".\day2")
    newinput = day2.take_input("test2.txt")
    np.testing.assert_array_equal(newinput, TEST_ARRAY)

