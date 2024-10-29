#!/usr/bin/python3
def text_indentation(text):
    """Prints text with two new lines after each of: ., ?, and :."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    length = len(text)

    while i < length:
        result += text[i]
        if text[i] in '.?:':
            result += '\n\n'  # Add two new lines after the character
            # Skip any whitespace that follows the punctuation
            while i + 1 < length and text[i + 1] == ' ':
                i += 1
        i += 1

    # Strip leading/trailing whitespace from each line
    # and split by lines to print without extra blank lines
    print('\n'.join(
        line.strip() for line in result.splitlines() if line.strip()))
