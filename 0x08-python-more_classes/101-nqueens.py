#!/usr/bin/python3
import sys
"""define functions"""

def is_safe(board, row, col, n):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    # If all queens are placed then return true
    if col >= n:
        print_solution(board, n)
        return True

    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, n) or res
            board[i][col] = 0  # Backtrack

    return res

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("No solution exists")

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                sys.stdout.write("Q ")
            else:
                sys.stdout.write(". ")
        sys.stdout.write("\n")
    sys.stdout.write("\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(n)

if __name__ == "__main__":
    main()
