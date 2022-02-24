#!/usr/bin/env python3

class BankAccount():
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value

    def __str__(self):
        return "Your current balance is {:.2f} euro".format(self.balance)
