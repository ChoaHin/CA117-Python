#!/usr/bin/env python3

import sys

try:
    with open(sys.argv[1], "r") as f:
        best_score = 0
        best_name = list()
        for line in f:
            [score, name] = line.strip().split(" ", 1)
            try:
                if int(score) > best_score:
                    best_score = int(score)
                    best_name = list()
                if int(score) == best_score:
                    best_name.append(name)
            except ValueError:
                print(f'Invalid mark {score} encountered. Skipping.')

        best_name = ", ".join(best_name)
        print(f"Best student(s): {best_name}\nBest mark: {best_score}")

except(FileNotFoundError()):
    print(f"The file {sys.argv[1]} could not be opened.")
