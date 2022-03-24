#!/usr/bin/env python3

class Triathlete():
    def __init__(self, name, tid):
        self.d = {}
        self.name = name
        self.tid = tid

    def __str__(self):
        a = []
        a.append('Name: {}'.format(self.name))
        a.append('ID: {}'.format(self.tid))
        # total = sum(self.d.values())
        # a.append('Race time: {}'.format(total))
        return "\n".join(a)

    def add_time(self, obj, time):
        self.d[obj] = time

    def get_time(self, obj):
        return self.d[obj]

    def __eq__(self, other):
        return sum(self.d.values()) == sum(other.d.values())

    def __gt__(self, other):
        return sum(self.d.values()) > sum(other.d.values())

def sorter(x):
    return x[1]

class Triathlon():
    def __init__(self):
        self.d = {}

    def add(self, t):
        self.d[t.name] = t

    def remove(self, tid):
        del self.d[tid]

    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        return None

    def __str__(self):
        a = []
        for key in sorted(self.d):
            a.append(str(self.d[key]))
        return '\n'.join(a)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
