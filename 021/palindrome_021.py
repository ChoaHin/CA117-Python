#1/usr/env python3

import sys

def palindrome(s):
    s = "".join(char for char in s if char.isalnum()).lower()
    if s == s[::-1]:
        return True
    else:
        return False


for line in sys.stdin:
    line = line.strip()
    print(palindrome(line))
