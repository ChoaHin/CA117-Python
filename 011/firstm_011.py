#!/usr/bin/env python3

import sys

def upper_m(s):
    return s.replace("m", "M", 1)


for line in sys.stdin:
    print(upper_m(line).strip())
