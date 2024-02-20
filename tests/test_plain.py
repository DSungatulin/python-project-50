from gendiff.formatters.plain import get_plain_view, get_plained


def test_get_plain_view():
    assert get_plain_view('path_to_property', 'ADDED', None, 'new_value') == "Property 'path_to_property' was added with value: 'new_value'"
    assert get_plain_view('path_to_property', 'REMOVED', 'old_value', None) == "Property 'path_to_property' was removed"
    assert get_plain_view('path_to_property', 'CHANGED', 'old_value', 'new_value') == "Property 'path_to_property' was updated. From 'old_value' to 'new_value'"

def test_get_plained():
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
        "Property 'property' was added with value: 'new_value'",
        "Property 'another_property' was removed",
        "Property 'yet_another_property' was updated. From 'old_value' to 'new_value'"
    ])
    assert get_plained(diff) == expected_output