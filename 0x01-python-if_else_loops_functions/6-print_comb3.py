#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        if i < j:
            end_char = ", " if not (i == 8 and j == 9) else "\n"
            print("{:02d}".format(i) + "{:02d}".format(j), end=end_char)
