import argparse
import json
import yaml


def parse_file():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output (default: \'stylish\')',
    )
    return parser.parse_args()


def determine_file_format(filepath):
    with open(filepath) as file:
        if filepath.endswith('.json'):
            data = json.load(file)
        elif filepath.endswith('.yml') or filepath.endswith('.yaml'):
            data = yaml.safe_load(file)
        else:
            raise TypeError("Invalid file format!")
        return data
