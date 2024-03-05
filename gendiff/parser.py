import json
import yaml
import os


def get_file_format(filepath):
    _, file_format = os.path.splitext(filepath)
    return file_format[1:]


def read_file_data(filepath):
    with open(filepath) as file:
        file_format = get_file_format(filepath)
        if file_format == 'json':
            return json.load(file)
        elif file_format == 'yaml' or 'yml':
            return yaml.load(file, Loader=yaml.Loader)
        else:
            raise TypeError("Invalid file format!")
