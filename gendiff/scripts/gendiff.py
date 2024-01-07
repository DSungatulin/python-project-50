#!/usr/bin/env python3
from gendiff.define_diff import generate_diff
from gendiff import parser


def main():
    first_file, second_file = parser.parse_file()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
