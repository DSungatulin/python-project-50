import argparse
import json
import yaml


def parse_file():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output (default: \'stylish\')',
    )
    return parser.parse_args()


def get_file_format(filepath):
    if filepath.endswith('.json'):
        return 'json'
    elif filepath.endswith('.yml') or filepath.endswith('.yaml'):
        return 'yaml'
    else:
        raise TypeError("Invalid file format!")


def read_file_data(filepath):
    with open(filepath) as file:
        if get_file_format(filepath) == 'json':
            return json.load(file)
        elif get_file_format(filepath) == 'yaml':
            return yaml.safe_load(file)
        else:
            raise TypeError("Invalid file format!")
