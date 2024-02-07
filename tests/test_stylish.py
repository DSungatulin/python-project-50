
from gendiff.formatters.stylish import get_stylish_view, form_string, get_stylished


def test_get_stylish_view():
    assert get_stylish_view('key', 'value', '+ ', 1, '  ') == "  + key: 'value'"
    assert get_stylish_view('key', {'nested_key': 'value'}, '    ', 1, '    ') == "        key: {\n        nested_key: 'value'\n      }"

def test_form_string():
    assert form_string('key', 'ADDED', None, 'new_value', 1, '    ') == "    + key: 'new_value'"
    assert form_string('key', 'REMOVED', 'old_value', None, 1, '    ') == "    - key: 'old_value'"
    assert form_string('key', 'CHANGED', 'old_value', 'new_value', 1, '    ') == "    - key: 'old_value'\n    + key: 'new_value'"
    assert form_string('key', 'UNCHANGED', 'old_value', 'old_value', 1, '    ') == "      key: 'old_value'"

def test_get_stylished():
    diff = [
        {
            'key': 'property',
            'action': 'ADDED',
            'old value': None,
            'new value': 'new_value',
            'nested': None
        },
        {
            'key': 'another_property',
            'action': 'REMOVED',
            'old value': 'old_value',
            'new value': None,
            'nested': None
        },
        {
            'key': 'yet_another_property',
            'action': 'CHANGED',
            'old value': 'old_value',
            'new value': 'new_value',
            'nested': None
        }
    ]
    expected_output = "\n".join([
        "{",
        "  + property: 'new_value'",
        "  - another_property: 'old_value'",
        "  - yet_another_property: 'old_value'",
        "  + yet_another_property: 'new_value'",
        "}"
    ])
    assert get_stylished(diff) == expected_output
