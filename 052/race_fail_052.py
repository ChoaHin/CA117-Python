#!/usr/bin/env python3

import sys

def seconds(d):
    [mins, secs] = d.split(':')
    if mins.isnumeric() and secs.isnumeric():
        total = (int(mins) * 60 + int(secs))
        return total

def sorter(t):
    return seconds(t[1])
    
d = {}
for line in sys.stdin:
    try:
        tokens = line.strip().split()
        name, times = tokens[:-5], tokens[-5:]
        d[" ".join(name)]= min(times, key=seconds)
    except ValueError():
        continue

winner = min(d.items(), key=sorter)
name, time = winner
print(f'{name} : {time}')