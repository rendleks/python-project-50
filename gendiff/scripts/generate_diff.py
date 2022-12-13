#!/usr/bin/env python
import json
import pprint


def generate_diff(first_file, second_file):
    first_file = json.load(open(first_file))
    second_file = json.load(open(second_file))
    result = {}
    common_keys = sorted(first_file | second_file)
    print(common_keys)

    for key in common_keys:
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                result[f"  {key}"] = first_file[key]
            else:
                result[f"- {key}"] = first_file[key]
                result[f"+ {key}"] = second_file[key]
        elif key in first_file and key not in second_file:
            result[f"- {key}"] = first_file[key]
        elif key not in first_file and key in second_file:
            result[f"+ {key}"] = second_file[key]
        
    return result
    


pprint.pprint(generate_diff("C:\\Users\\internetshop17\\pars\\python-project-50\\gendiff\\scripts\\file1.json", "C:\\Users\\internetshop17\\pars\\python-project-50\\gendiff\\scripts\\file2.json"))



