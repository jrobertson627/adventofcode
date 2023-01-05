import numpy as np
import day5_2022 as day5
CARGO_BEGIN = [['z', 'n'], ['m', 'c', 'd'], ['p']]
CARGO_INSTRUCTIONS = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]] # num, origin stack, end stack
CARGO_END1 = [['c'], ['m'], ['p', 'd', 'n', 'z']]
CARGO_END2 = [['m'],['c'],['d', 'n', 'z', 'p']]
CARGO_TOPS1 = 'cmz'

def test_change_stacks_pt1():
    my_cargo = day5.all_movements(CARGO_BEGIN, CARGO_INSTRUCTIONS, 1)
    np.testing.assert_equal(my_cargo, CARGO_END1)
    cargo2 = day5.all_movements(CARGO_BEGIN, CARGO_INSTRUCTIONS, 2)
    np.testing.assert_equal(cargo2, CARGO_END2)


def test_end_tops():
    my_top = day5.determine_top(CARGO_END1)
    np.testing.assert_string_equal(my_top, CARGO_TOPS1)