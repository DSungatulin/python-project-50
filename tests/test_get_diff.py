from fixtures.expected_result_for_test_get_diff import expected_result
from gendiff.diff_determinant import get_diff


def test_get_diff():
    dict1 = {'a': 1, 'b': 2, 'c': {'x': 10, 'y': 20}}
    dict2 = {'a': 1, 'b': 3, 'd': 4, 'c': {'x': 10, 'z': 30}}
    assert get_diff(dict1, dict2) == expected_result
