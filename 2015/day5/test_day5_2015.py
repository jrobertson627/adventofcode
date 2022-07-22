import day5_2015 as day5

TEST_STRING_1 = "ugknbfddgicrmopn"
TEST_RESULT_1 = 1

TEST_STRING_2 = "aaa"
TEST_RESULT_2 = 1

TEST_STRING_3 = "jchzalrnumimnmhp"
TEST_RESULT_3 = 0

TEST_STRING_4 = "haegwjzuvuyypxyu"
TEST_RESULT_4 = 0

TEST_STRING_5 = "dvszwmarrgswjxmb"
TEST_RESULT_5 = 0

TEST_STRING_6 = "qjhvhtzxzqqjkmpb"
TEST_RESULT_6 = 1

TEST_STRING_7 = "xxyxx"
TEST_RESULT_7 = 1

TEST_STRING_8 = "uurcxstgmygtbstg"
TEST_RESULT_8 = 0

TEST_STRING_9 = "ieodomkazucvgmuy"
TEST_RESULT_9 = 0

def test_check_vowels():
    result1 = day5.check_vowels(TEST_STRING_1)
    assert result1 == TEST_RESULT_1

    result2 = day5.check_vowels(TEST_STRING_2)
    assert result2 == TEST_RESULT_2

    result5 = day5.check_vowels(TEST_STRING_5)
    assert result5 == TEST_RESULT_5

def test_check_doubles():
    result1 = day5.check_doubles(TEST_STRING_1)
    assert result1 == TEST_RESULT_1

    result2 = day5.check_doubles(TEST_STRING_2)
    assert result2 == TEST_RESULT_2

    result3 = day5.check_doubles(TEST_STRING_3)
    assert result3 == TEST_RESULT_3

def test_check_bad_strings():
    result1 = day5.check_bad_strings(TEST_STRING_1)
    assert result1 == TEST_RESULT_1

    result2 = day5.check_bad_strings(TEST_STRING_2)
    assert result2 == TEST_RESULT_2

    result4 = day5.check_bad_strings(TEST_STRING_4)
    assert result4 == TEST_RESULT_4

def test_check_pairs():
    result6 = day5.check_pairs(TEST_STRING_6)
    assert result6 == TEST_RESULT_6

    result7 = day5.check_pairs(TEST_STRING_7)
    assert result7 == TEST_RESULT_7

    result8 = day5.check_pairs(TEST_STRING_8)
    assert result8 == 1

    result9 = day5.check_pairs(TEST_STRING_9)
    assert result9 == TEST_RESULT_9

    result2 = day5.check_pairs(TEST_STRING_2)
    assert result2 == 0

def test_repeat_letters():
    result6 = day5.check_repeat_letters(TEST_STRING_6)
    assert result6 == TEST_RESULT_6

    result7 = day5.check_repeat_letters(TEST_STRING_7)
    assert result7 == TEST_RESULT_7

    result8 = day5.check_repeat_letters(TEST_STRING_8)
    assert result8 == TEST_RESULT_8

    result9 = day5.check_repeat_letters(TEST_STRING_9)
    assert result9 == 1