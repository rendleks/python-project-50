#!/usr/bin/env python3
import argparse


def help():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, dest="first_file")
    parser.add_argument('second_file', type=str, dest="second_file")
    parser.add_argument('-f', '--format', help='set format of output', type=str, choices=['plain', 'json'], default="json", dest='format')
    parser.parse_args()



