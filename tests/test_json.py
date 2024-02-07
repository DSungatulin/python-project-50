import json
from gendiff.formatters.json import json_format


def test_json_format():
    data = {
        'key': 'value',
        'list': [1, 2, 3],
        'nested': {
            'another_key': 'another_value'
        }
    }
    expected_output = json.dumps(data, indent=2)
    assert json_format(data) == expected_output
