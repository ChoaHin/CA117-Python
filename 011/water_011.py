#!/usr/bin/env python3

import sys

[water, buckets] = sys.stdin.readlines()
buckets = buckets.split()

filled = 0
total = 0
for token in buckets:
    total += int(token)
    if total <= int(water):
        filled += 1

print(filled)
