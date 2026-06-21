# Time Complexity: O(N!)
# Space Complexity: O(N)
# Explanation: Use backtracking to place queens column by column. Use three hash arrays (or bitmasks) to track attacked rows, upper diagonals, and lower diagonals. If placing a queen is safe, update hashes, recurse for next column, and then backtrack.

def totalNQueens(n: int) -> int:
    count = 0
    leftRow = [0] * n
    upperDiag = [0] * (2 * n - 1)
    lowerDiag = [0] * (2 * n - 1)
    def solve(col):
        nonlocal count
        if col == n:
            count += 1
            return
        for row in range(n):
            if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:
                leftRow[row] = 1
                lowerDiag[row + col] = 1
                upperDiag[n - 1 + col - row] = 1
                solve(col + 1)
                leftRow[row] = 0
                lowerDiag[row + col] = 0
                upperDiag[n - 1 + col - row] = 0
    solve(0)
    return count

