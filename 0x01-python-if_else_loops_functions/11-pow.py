#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    result = 1
    abs_b = abs(b)
    for _ in range(abs_b):
        result *= a
    if b < 0:
        return 1 / result
    return result
