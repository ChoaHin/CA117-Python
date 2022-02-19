#!/usr/bin/env python3

import sys
[total, room] = sys.stdin.read().split(" ", 1)

total = [n for n in range(1, int(total) + 1)]
room = room.split()

for n in room:
    if int(n) in total:
        total.remove(int(n))

if len(total):
    print(total[0])
else:
    print('no room')
