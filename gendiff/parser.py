import argparse
import json
import yaml


def parse_file():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args

def determine_file_format(filepath):
    if filepath.endswith('json'):
        data = json.load(open(filepath))
    elif filepath.endswith('yml') or filepath.endswith('yaml'):
        data = yaml.safe_load(open(filepath))
    else:
        raise ValueError("Invalid file format!")
    return data
