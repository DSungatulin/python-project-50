from gendiff.json_diff import open_json
from gendiff.yaml_diff import open_yaml


def convert_bool_value(val):
    bool_value = {'True': 'true', 'False': 'false'}
    if isinstance(val, bool):
        return bool_value[str(val)]
    else:
        return val


def format_decoder(filepath):
    if filepath.endswith('json'):
        return open_json(filepath)
    elif filepath.endswith('yml') or filepath.endswith('yaml'):
        return open_yaml(filepath)
    else:
        raise ValueError("Invalid file format!")
