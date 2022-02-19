#!/usr/bin/env python3

import sys

es = ["ch", "sh", "x", "s", "z", "o"]
vovel = ["a", "e", "i", "o", "u"]
ies = ["fe", "f"]

def plural(s):
    left = s[:-2]
    right = s[-2:]
    if right in es or right[-1] in es:
        return(left + right + "es")
    elif right[0] not in vovel and right[-1] == "y":
        return(left + right[0] + "ies")
    elif right in ies:
        return(left + "ves")
    elif right[-1] in ies:
        return(left + right[0] + "ves")
    elif right[-1] == "o":
        return(left + right + "es")
    else:
        return(left + right + "s")


for line in sys.stdin:
    line = line.strip()
    print(plural(line))
