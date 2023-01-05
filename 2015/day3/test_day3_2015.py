import day3_2015 as day3

TEST_ARRAY = [[0, 0], [0, 0]]

TEST_INPUT_1 = ">"
TEST_RESULT_1 = 2

TEST_INPUT_2 = "^>v<"
TEST_RESULT_2 = 4

TEST_INPUT_3 = "^v^v^v^v^v"
TEST_RESULT_3 = 2

TEST_INPUT_4 = "^v"
TEST_RESULT_4 = 3

TEST_INPUT_5 = "^>v<"
TEST_RESULT_5 = 3

TEST_INPUT_6 = "^v^v^v^v^v"
TEST_RESULT_6 = 11


def test_calc_unique_houses_pt1():
    result1 = day3.calculate_unique_houses_pt1(TEST_INPUT_1)
    assert result1 == TEST_RESULT_1
    result2 = day3.calculate_unique_houses_pt1(TEST_INPUT_2)
    assert result2 == TEST_RESULT_2
    result3 = day3.calculate_unique_houses_pt1(TEST_INPUT_3)
    assert result3 == TEST_RESULT_3

def test_calc_unique_houses_pt2():
    result4 = day3.calculate_unique_houses_pt2(TEST_INPUT_4)
    assert result4 == TEST_RESULT_4
    result5 = day3.calculate_unique_houses_pt2(TEST_INPUT_5)
    assert result5 == TEST_RESULT_5
    result6 = day3.calculate_unique_houses_pt2(TEST_INPUT_6)
    assert result6 == TEST_RESULT_6