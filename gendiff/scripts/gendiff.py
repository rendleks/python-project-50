#!/usr/bin/env python
import argparse
from gendiff import generate_diff


def help():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', type=str, default="json", dest='format')
    return parser.parse_args()


def main():
    parse = help()
    print(
        generate_diff.stringify(parse.first_file, parse.second_file, format=parse.format)
        )


if __name__ == "__main__":
    main()

