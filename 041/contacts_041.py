#/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

phone_book = {}
for line in lines:
    [name, phone] = line.strip().split()
    phone_book[name] = phone

for line in sys.stdin:
    line = line.strip()
    try:
        print(
            f'Name: {line}\n'
            'Phone:', phone_book[line])
    except KeyError:
        print(f'Name: {line}\nNo such contact')
