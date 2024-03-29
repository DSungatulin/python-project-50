import argparse


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
