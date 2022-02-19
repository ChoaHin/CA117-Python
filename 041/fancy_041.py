#/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

phone_book = {}
for line in lines:
    [name, info] = line.strip().split(' ', 1)
    phone_book[name] = info.split()

for line in sys.stdin:
    line = line.strip()
    try:
        print('Name:', line)
        print('Phone:', phone_book[line][0])
        print('Email:', phone_book[line][1])
    except KeyError:
        print('No such contact')
