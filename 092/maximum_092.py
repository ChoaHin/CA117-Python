#!/usr/bin/env python3

def maximum(ls):
    if len(ls) == 1:
        return ls[0]
    tail = maximum(ls[1:])
    return ls[0] if ls[0] > tail else tail
