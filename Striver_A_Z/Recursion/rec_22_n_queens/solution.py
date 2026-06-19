# Time Complexity: O(N!)
# Space Complexity: O(N^2)
# Explanation: Place queens column by column. Keep track of safe rows and diagonals using hashing arrays: `leftRow`, `lowerDiagonal`, `upperDiagonal`. If safe, place queen, update hashes, and recurse.

def solveNQueens(n: int) -> List[List[str]]:
    ans = []
    board = [["."] * n for _ in range(n)]
    leftRow = [0] * n
    upperDiagonal = [0] * (2 * n - 1)
    lowerDiagonal = [0] * (2 * n - 1)
    def solve(col):
        if col == n:
            ans.append(["".join(r) for r in board])
            return
        for row in range(n):
            if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:
                board[row][col] = 'Q'
                leftRow[row] = 1; lowerDiagonal[row + col] = 1; upperDiagonal[n - 1 + col - row] = 1
                solve(col + 1)
                board[row][col] = '.'
                leftRow[row] = 0; lowerDiagonal[row + col] = 0; upperDiagonal[n - 1 + col - row] = 0
    solve(0)
    return ans

