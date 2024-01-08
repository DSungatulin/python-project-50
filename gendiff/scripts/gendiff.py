#!/usr/bin/env python3
from gendiff.define_diff import generate_diff
from gendiff.parser import parse_file


def main():
    args = parse_file()
    file_difference = generate_diff(args.first_file, args.second_file)
    return print(file_difference)


if __name__ == '__main__':
    main()
