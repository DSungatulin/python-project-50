import argparse
import json
import yaml
import os


def parse_file(first_file, second_file):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    
    file_ext = os.path.splitext(first_file)[1]
    if file_ext == 'json':
        deserialized_first_file, deserialized_second_file = json.load(open(args.first_file, args.second_file))
    elif file_ext == 'yml' or file_ext == 'yaml':
        deserialized_first_file, deserialized_second_file = yaml.safe_load(open(args.first_file, args.second_file))
    else:
        raise ValueError("Invalid file format!")
    return deserialized_first_file, deserialized_second_file