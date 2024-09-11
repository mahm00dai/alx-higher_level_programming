#!/usr/bin/python3

def remove_char_at(str, n):
    # Check if n is within the valid range of indices
    if n < 0 or n >= len(str):
        return str
    # Return a new string with the character at position n removed
    return str[:n] + str[n+1:]
