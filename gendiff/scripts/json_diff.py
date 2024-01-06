import json


def open_json(file_path):
    deserialized_file = json.load(open(file_path))
    return deserialized_file