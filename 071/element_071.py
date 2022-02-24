#!/usr/bin/env python3

class Element():
    def set_attributes(self, number, name, symbol, boiling_point):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.bp = boiling_point

    def print_attributes(self):
        print(
            f'Number: {self.number}\n'
            f'Name: {self.name}\n'
            f'Symbol: {self.symbol}\n'
            f'Boiling point: {self.bp} K')
