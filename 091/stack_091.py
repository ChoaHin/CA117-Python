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
