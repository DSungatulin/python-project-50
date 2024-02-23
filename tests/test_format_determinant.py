from gendiff.formatters.format_determinant import get_data_format_plain


def test_get_data_format_plain_dict():
    assert get_data_format_plain({"key": "value"}) == '[complex value]'


def test_get_data_format_plain_bool():
    assert get_data_format_plain(True) == 'true'
    assert get_data_format_plain(False) == 'false'


def test_get_data_format_plain_string():
    assert get_data_format_plain("hello") == "'hello'"


def test_get_data_format_plain_none():
    assert get_data_format_plain(None) == 'null'


def test_get_data_format_plain_other_types():
    assert get_data_format_plain(123) == '123'
    assert get_data_format_plain(12.3) == '12.3'
