import day4_2015 as day4

TEST_INPUT_1 = "abcdef"
TEST_RESULT_1 = 609043

TEST_INPUT_2 = "pqrstuv"
TEST_RESULT_2 = 1048970

def test_five_zeros():
    result1 = day4.find_five_zeroes(TEST_INPUT_1)
    assert result1 == TEST_RESULT_1

    result2 = day4.find_five_zeroes(TEST_INPUT_2)
    assert result2 == TEST_RESULT_2