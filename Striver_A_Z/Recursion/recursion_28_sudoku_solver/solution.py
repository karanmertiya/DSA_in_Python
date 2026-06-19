# Time Complexity: O(9^(n*n))
# Space Complexity: O(1) excluding recursion stack
# Explanation: Iterate through each cell. If it's empty, try placing digits '1' to '9'. For each digit, check if it's valid in its row, column, and 3x3 subgrid. If valid, place it and recursively try to solve the rest. If a path leads to a solution, return true. Otherwise, backtrack (remove digit).

def solveSudoku(board: List[List[str]]) -> None:
    def isValid(row, col, c):
        for i in range(9):
            if board[i][col] == c: return False
            if board[row][i] == c: return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c: return False
        return True
    def solve():
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in map(str, range(1, 10)):
                        if isValid(i, j, c):
                            board[i][j] = c
                            if solve(): return True
                            board[i][j] = '.'
                    return False
        return True
    solve()

