#!/usr/bin/python3
import sys


def print_solutions(solutions):
    """Print the solutions in the specified format."""
    for solution in solutions:
        print(solution)


def is_not_under_attack(row, col, queens):
    """Check if the position (row, col) is under
    attack by any existing queen."""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def place_queen(n, row, queens, solutions):
    """Place queens using backtracking."""
    if row == n:
        solutions.append(list(queens))
        return

    for col in range(n):
        if is_not_under_attack(row, col, queens):
            queens.append((row, col))
            place_queen(n, row + 1, queens, solutions)
            queens.pop()


def nqueens(n):
    """Solve the N queens puzzle and return all solutions."""
    solutions = []
    place_queen(n, 0, [], solutions)
    return solutions


def main():
    """Main function to handle command line arguments
    and solve the N queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solutions = nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
