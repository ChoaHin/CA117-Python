#!/usr/bin/env python3

import sys

try:
    with open(sys.argv[1], "r") as f:
        best_score = 0
        best_name = str()
        for line in f:
            [score, name] = line.strip().split(" ", 1)
            try:
                if int(score) > best_score:
                    best_score = int(score)
                    best_name = name
            except ValueError:
                print(f'Invalid mark {score} encountered. Skipping.')
        print(f"Best student: {best_name}\nBest mark: {best_score}")

except(FileNotFoundError()):
    print(f"The file {sys.argv[1]} could not be opened.")
