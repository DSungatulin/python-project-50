import json


def open_json(filepath):
    deserialized_file = json.load(open(filepath))
    return deserialized_file
