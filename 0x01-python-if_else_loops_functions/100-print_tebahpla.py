#!/usr/bin/python3

def print_tebahpla():
    result = ''
    for i in range(26):
        if i % 2 == 0:
            result += '{}'.format(chr(122 - i))
        else:
            result += '{}'.format(chr(90 - i))
    print(result, end='')


print_tebahpla()
