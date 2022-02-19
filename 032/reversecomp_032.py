#!/usr/bin/env python3

import sys

# Binary search (adapted from CA116)
def binsearch(query, sorted_list):

    '''Return True if query in sorted_list else False'''

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        # print(f'{low} {mid} {high}')

        if sorted_list[mid] < query:
            # Search RHS
            low = mid + 1

        elif sorted_list[mid] > query:
            # Search LHS
            high = mid - 1

        else:
            # Found it
            return True

    # Not found
    return False


sorted_list = sys.stdin.read().split()
lower_sorted_list = [word.lower() for word in sorted_list]
reversecomp = list()
for line in sorted_list:
    if len(line) >= 5:
        if binsearch(line[::-1].lower(), lower_sorted_list):
            reversecomp.append(line)

print(reversecomp)
