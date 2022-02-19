#!/usr/bin/env python3

def swap_unique_keys_values(d):
    value = list(d.values())
    unique = [v for v in value if value.count(v) == 1]
    new_dict = {b: a for (a, b) in d.items() if b in unique}
    return new_dict
