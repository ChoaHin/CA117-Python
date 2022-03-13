#!/usr/bin/env python3

def reverse_list(ls):
    if ls == []:
        return []
    return reverse_list(ls[1:]) + [ls[0]]
