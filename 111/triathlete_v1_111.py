#!/usr/bin/env python3

class Triathlete():
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        a = []
        a.append('Name: {}'.format(self.name))
        a.append('ID: {}'.format(self.tid))
        return "\n".join(a)
