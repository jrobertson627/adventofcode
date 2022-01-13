import os
import day1
import numpy as np

TEST_ARRAY = np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
TEST__RESULT1 = 7
TEST__RESULT2 = 5

def test_getNumLarger_Part1():
    num_larger = day1.getNumLarger_Part1(TEST_ARRAY)
    assert num_larger == TEST__RESULT1
    
def test_getLargerTrio_Part2():
    trio_larger = day1.getLargerTrio_Part2(TEST_ARRAY)
    assert trio_larger == TEST__RESULT2
    
def test_read_input():
    os.chdir(".\day1")
    new_array = day1.read_input('test1.txt')
    np.testing.assert_array_equal(new_array, TEST_ARRAY)


