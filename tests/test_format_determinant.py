from gendiff.formatters.format_determinant import get_data_format

def test_get_data_format():
    assert get_data_format(10) == "10"
    assert get_data_format(True) == "true"
    assert get_data_format("hello") == "hello"
    assert get_data_format(None) == "null"
    assert get_data_format({1: [2, 3]}) == "[complex value]"