#!/usr/bin/env python3

def minimum(ls):
    if len(ls) == 1:
        return ls[0]
    tail = minimum(ls[1:])
    return ls[0] if ls[0] < tail else tail
