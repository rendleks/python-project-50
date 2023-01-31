from gendiff import generate_diff
import json
import os


def test_simple():
    file1 = json.load(open(os.path.join('tests', 'fixtures', 'file1.json')))
    file2 = json.load(open(os.path.join('tests', 'fixtures', 'file2.json')))

    expected = """
    {
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
    }
    """

    print(generate_diff.stringify(file1, file2))

test_simple()