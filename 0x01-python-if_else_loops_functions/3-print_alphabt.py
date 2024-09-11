#!/usr/bin/python3

alphabet = "".join(
    "{0}".format(chr(i)) for i in range(97, 123)
    if chr(i) not in ('q', 'e')
)

print(alphabet, end="")
