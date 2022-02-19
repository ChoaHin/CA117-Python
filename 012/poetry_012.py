#!/usr/bin/env python3

import sys

text = []
length = 0
for line in sys.stdin:
    line = line.strip()
    if len(line) > length:
        length = len(line)
    text.append(line)

for line in text:
    print(f'{line:^{length}}')
