#!/usr/bin/env python
import argparse
from gendiff import scripts


def help():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', type=str, default="json", dest='format')
    return parser.parse_args()


def main():
    scripts.generate_diff.main()


if __name__ == "__main__":
    main()


