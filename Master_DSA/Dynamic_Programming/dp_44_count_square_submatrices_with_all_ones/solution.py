# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
# Explanation: Let `dp[i][j]` be the size of the largest square ending at `(i, j)`. If `matrix[i][j] == 1`, then `dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]})`. The total number of squares is the sum of all elements in the `dp` matrix.

def countSquares(matrix):
    r, c = len(matrix), len(matrix[0])
    dp = [[0] * c for _ in range(r)]
    ans = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                if i == 0 or j == 0: dp[i][j] = 1
                else: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                ans += dp[i][j]
    return ans

