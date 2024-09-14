#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4  # Import the compiled module
    names = dir(hidden_4)  # Get the list of names in the module

    for name in sorted(names):  # Sort the names alphabetically
        if not name.startswith("__"):  # Ignore names that start with "__"
            print(name)
