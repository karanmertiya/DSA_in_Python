# Time Complexity: O(N!)
# Space Complexity: O(N^2)
# Explanation: Backtracking. Place queen column by column. To optimize collision checking to O(1), use 3 arrays/hashmaps: `leftRow`, `upperDiagonal`, and `lowerDiagonal`.

def solveNQueens(n: int) -> List[List[str]]:
    ans = []
    board = [['.'] * n for _ in range(n)]
    leftRow, upperDiag, lowerDiag = [0]*n, [0]*(2*n-1), [0]*(2*n-1)
    def solve(col):
        if col == n:
            ans.append([''.join(row) for row in board])
            return
        for row in range(n):
            if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:
                board[row][col] = 'Q'
                leftRow[row] = 1; lowerDiag[row + col] = 1; upperDiag[n - 1 + col - row] = 1
                solve(col + 1)
                board[row][col] = '.'
                leftRow[row] = 0; lowerDiag[row + col] = 0; upperDiag[n - 1 + col - row] = 0
    solve(0)
    return ans

