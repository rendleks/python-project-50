#!/usr/bin/env python
import itertools
import json



def key_in_dicts(key, lst1, lst2,  replace=' ', spacer_count=2):
    offset = replace * spacer_count
    if key in lst1 and key in lst2:
        if lst1.setdefault(key, '') == lst2.setdefault(key, ''):
            return f"{offset}  {key}: {lst1[key]}"
        elif lst1.setdefault(key, ''):
            return (f"{offset}- {key}: {lst1[key]}\n{offset}+ {key}: {lst2[key]}")
    elif key in lst1 and key not in lst2:
        return f"{offset}- {key}: {lst1[key]}"
    elif key not in lst1 and key in lst2:
        return f"{offset}+ {key}: {lst2[key]}"


def stringify(file1, file2, format="json"):
    lst1 = json.load(open(file1))
    lst2 = json.load(open(file2))
    uniq_keys = sorted(lst1.keys() | lst2.keys())
    lines = []
    for key in uniq_keys:
        lines.append(f"{key_in_dicts(key, lst1, lst2)}")
    result = itertools.chain("{", lines,"}")
    return '\n'.join(result)

