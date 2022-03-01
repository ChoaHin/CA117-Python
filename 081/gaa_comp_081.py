#!/usr/bin/env python3

class Score():
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __str__(self):
        return f'{self.goals} goal(s) and {self.points} point(s)'

    def total_point(self):
        return self.goals * 3 + self.points

    def __eq__(self, other):
        return self.total_point() == other.total_point()

    def __gt__(self, other):
        return self.total_point() > other.total_point()

    def __ge__(self, other):
        return self.total_point() >= other.total_point()
