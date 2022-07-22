import day2_2015 as day2
import unittest

TEST_INPUT_1 = [2, 3, 4]
TEST_RESULT_1 = 58
TEST_RESULT_AREA_1 = 52
TEST_RESULT_SLACK_1 = 6
TEST_RESULT_RIBBON_1 = 34

TEST_INPUT_2 = [1, 1, 10]
TEST_RESULT_2 = 43
TEST_RESULT_AREA_2 = 42
TEST_RESULT_SLACK_2 = 1
TEST_RESULT_RIBBON_2 = 14

def test_slack():
    slack_1 = day2.calculate_slack(TEST_INPUT_1)
    assert slack_1 == TEST_RESULT_SLACK_1
    slack_2 = day2.calculate_slack(TEST_INPUT_2)
    assert slack_2 == TEST_RESULT_SLACK_2

def test_area():
    area1 = day2.calculate_area(TEST_INPUT_1)
    assert area1 == TEST_RESULT_AREA_1
    area_2 = day2.calculate_area(TEST_INPUT_2)
    assert area_2 == TEST_RESULT_AREA_2

def test_total_needed():
    sum = day2.calculate_slack(TEST_INPUT_1)
    sum+= day2.calculate_area(TEST_INPUT_1)
    assert sum == TEST_RESULT_1

def test_calculate_ribbon():
    ribbon_1 = day2.calculate_ribbon(TEST_INPUT_1)
    assert ribbon_1 == TEST_RESULT_RIBBON_1

    ribbon_2 = day2.calculate_ribbon(TEST_INPUT_2)
    assert ribbon_2 == TEST_RESULT_RIBBON_2

