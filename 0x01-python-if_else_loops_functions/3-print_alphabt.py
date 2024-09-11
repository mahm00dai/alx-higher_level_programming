#!/usr/bin/python3

# Generate the alphabet excluding 'q' and 'e'
alphabet = "".join(
    "{0}".format(chr(i)) for i in range(97, 123)
    if chr(i) not in ('q', 'e')
)

# Print the result without a newline at the end
print(alphabet, end="")
