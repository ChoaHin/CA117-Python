#!/usr/bin/env python3

import sys
[water, bucket] = sys.stdin.readlines()
bucket = bucket.split()

filled = 0
count = 0
for n in bucket:
    filled += int(n)
    if int(water) > filled:
        count += 1

print(count)
