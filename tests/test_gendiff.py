import pytest
from gendiff.generate_diff import stringify
import os


def get_fixture_path(file_name):
  current_dir = os.path.dirname(os.path.abspath(__file__))
  return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
  with open(file_path, 'r') as f:
      result = f.read()
  return result


file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False,
}


file2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io",
}

simple_data = read(get_fixture_path('simple.txt')).rstrip()


def test_simple():
  assert stringify(file1, file2) == simple_data
