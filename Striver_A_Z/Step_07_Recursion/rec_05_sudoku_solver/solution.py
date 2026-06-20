# Time Complexity: O(9^(n*n))
# Space Complexity: O(1) auxiliary
# Explanation: Backtracking. Find first empty cell, try placing 1-9. Validate row, col, and 3x3 sub-grid. Recursively solve the rest. If it fails, backtrack.

def solveSudoku(board: List[List[str]]) -> None:
    def isValid(row, col, ch):
        for i in range(9):
            if board[i][col] == ch: return False
            if board[row][i] == ch: return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch: return False
        return True
    def solve():
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in '123456789':
                        if isValid(i, j, c):
                            board[i][j] = c
                            if solve(): return True
                            else: board[i][j] = '.'
                    return False
        return True
    solve()

