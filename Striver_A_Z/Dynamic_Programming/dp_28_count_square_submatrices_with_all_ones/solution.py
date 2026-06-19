# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# Explanation: `dp[i][j]` is the size of the largest square ending at `(i, j)`. It also represents the number of squares ending at `(i, j)`. `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1` if `matrix[i][j] == 1`.

def countSquares(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    dp = [[0]*m for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i == 0 or j == 0: dp[i][j] = 1
                else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                total += dp[i][j]
    return total

