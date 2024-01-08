#!/usr/bin/env python3
from gendiff.define_diff import generate_diff
from gendiff import parser


def main():
    first_file, second_file = parser.parse_file()
    file_difference = generate_diff(first_file, second_file)
    return print(file_difference)


if __name__ == '__main__':
    main()
