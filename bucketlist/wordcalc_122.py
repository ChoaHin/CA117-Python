#!/usr/bin/env python3

import sys

def s_def(s, d):
    key, value = s.split()
    d[key] = int(value)
    return d

def calc(s, d):
    total = 0
    tmp = 0
    tokens = s.split()
    total = d[tokens[0]]
    i = 1
    while tokens[i] != '=' and i < len(tokens):
        if len(tokens[i]) <= 1:
            try:
                tmp = d[tokens[i + 1]]
            except KeyError:
                return print(f'{s} unknown')
            if tokens[i] == '+':
                total += tmp
            elif tokens[i] == '-':
                total -= tmp
        i += 1
    for k, v in d.items():
        if v == total:
            return print(f'{s} {k}')
    return print(f'{s} unknown')


d = {}
for line in sys.stdin:
    if line != "clear\n":
        (func, tokens) = line.strip().split(" ", 1)
        if func == "def":
            s_def(tokens, d)
        if func == "calc":
            calc(tokens, d)
    else:
        d = {}
