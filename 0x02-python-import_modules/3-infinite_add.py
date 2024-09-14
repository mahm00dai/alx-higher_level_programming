#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]  # Exclude the script name

    if len(argv) == 0:
        print(0)
    else:
        result = sum(int(arg) for arg in argv)
        print(result)
