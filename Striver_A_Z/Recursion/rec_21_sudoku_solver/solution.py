# Time Complexity: O(9^(N^2))
# Space Complexity: O(N^2)
# Explanation: Iterate through matrix. If empty, try '1' to '9'. Check `isValid` (row, col, 3x3 box). If valid, set it and recurse. If recursion returns true, puzzle solved. Else backtrack. If loop ends without returning true, return false.

def solveSudoku(board: List[List[str]]) -> None:
    def is_valid(r, c, ch):
        for i in range(9):
            if board[i][c] == ch: return False
            if board[r][i] == ch: return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch: return False
        return True
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for ch in '123456789':
                        if is_valid(i, j, ch):
                            board[i][j] = ch
                            if solve(): return True
                            board[i][j] = '.'
                    return False
        return True
    solve()

