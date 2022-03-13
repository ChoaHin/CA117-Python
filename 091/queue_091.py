#!/usr/bin/env python3

class Queue():
    def __init__(self):
        self.ls = []

    def enqueue(self, e):
        self.ls.append(e)

    def dequeue(self):
        return self.ls.pop(0)

    def first(self):
        return self.ls[0]

    def is_empty(self):
        return len(self.ls) == 0

    def __len__(self):
        return len(self.ls)
