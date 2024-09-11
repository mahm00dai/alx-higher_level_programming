#!/usr/bin/python3

# Create a string containing all lowercase letters
alphabet = ''.join(chr(i) for i in range(97, 123))

# Print the alphabet using the .format method
print('{}'.format(alphabet), end="")
