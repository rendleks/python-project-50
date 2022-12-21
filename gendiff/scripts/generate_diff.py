#!/usr/bin/env python
from itertools import zip_longest, chain
import itertools
import json


lst1 = json.load(open('gendiff/scripts/file1.json'))
lst2 = json.load(open('gendiff/scripts/file2.json'))


def key_in_dicts(key, lst1, lst2):
    if key in lst1 and key in lst2:
        if lst1.setdefault(key, '') == lst2.setdefault(key, ''):
            return f"  {key}: {lst1[key]}"
        elif lst1.setdefault(key, '') != lst2.setdefault(key, ''):
            return (f"- {key}: {lst1[key]}\n+ {key}: {lst2[key]}")
    elif key in lst1 and key not in lst2:
        return f"- {key}: {lst1[key]}"
    elif key not in lst1 and key in lst2:
        return f"+ {key}: {lst2[key]}"


def stringify(lst1, lst2, replace=' ', spacer_count=2):
    offset = replace * spacer_count
    uniq_keys = sorted(lst1.keys() | lst2.keys())
    lines = []
    for key in uniq_keys:
        lines.append(f"{offset}{key_in_dicts(key, lst1, lst2)}")
    result = itertools.chain("{",lines ,"}")
    return '\n'.join(result)


print(stringify(lst1, lst2))



