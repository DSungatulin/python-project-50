import json


def get_jsoned(current_data):
    return json.dumps(current_data, indent=2)
