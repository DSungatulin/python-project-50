import json
import yaml


def get_file_format(filepath):
    file = open(filepath)
    if filepath.endswith('.json'):
        return file, 'json'
    elif filepath.endswith('.yml') or filepath.endswith('.yaml'):
        return file, 'yaml'
    else:
        file.close()
        raise TypeError("Invalid file format!")


def read_file_data(filepath):
    file, file_format = get_file_format(filepath)
    if file_format == 'json':
        return json.load(file)
    elif file_format == 'yaml':
        return yaml.safe_load(file)
    else:
        raise TypeError("Invalid file format!")
