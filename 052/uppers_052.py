#!/usr/bin/env python3

import sys

max_len = 0
for line in sys.stdin:
    max_len = 0
    holder = ""
    for char in line:
        if char.isupper():
            holder += char
        else:
            if len(holder) > max_len:
                max_len = len(holder)
                upper = holder
            holder = ""
            count = 0
    print(upper)
