#!/usr/bin/env python3

class Stack():
    def __init__(self):
        self.ls = []

    def push(self, e):
        self.ls.append(e)

    def pop(self):
        return self.ls.pop()

    def top(self):
        return self.ls[-1]

    def is_empty(self):
        return len(self.ls) == 0

    def __len__(self):
        return len(self.ls)

def matcher(s):
    d = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    check = Stack()
    for char in s:
        if char in d.keys():
            check.push(char)
        elif char in d.values():
            if check.is_empty() or char != d[check.pop()]:
                return False
    return check.is_empty()
