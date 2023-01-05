import day2_2022 as day
import numpy as np

INPUT = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
INT_INPUT_PT1 = [[1, 2], [2, 1], [3, 3]]
INT_INPUT_PT2 = [[1, 1], [2, 1], [3, 1]]
POINTS_PT1 = [8, 1, 6]
POINTS_PT2 = [4, 1, 7]
TOT_POINTS_PT1 = 15
TOT_POINTS_PT2 = 12

def test_correct_array_pt1():
    my_input = day.transform_pt1(INPUT)
    assert np.allclose(my_input, INT_INPUT_PT1)
    my_input2 = day.transform_pt2(INPUT)
    assert np.allclose(my_input2, INT_INPUT_PT2)


def test_correct_points():
    my_points = day.get_points(INT_INPUT_PT1)
    assert np.allclose(my_points, POINTS_PT1)
    my_points2 = day.get_points(INT_INPUT_PT2)
    assert np.allclose(my_points2, POINTS_PT2)

def test_total_points():
    my_total = day.get_total(POINTS_PT1)
    assert my_total == TOT_POINTS_PT1
    my_total2 = day.get_total(POINTS_PT2)
    assert my_total2 == TOT_POINTS_PT2
