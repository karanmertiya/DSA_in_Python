# Time Complexity: O(R * C)
# Space Complexity: O(R * C) or O(C) optimized
# Explanation: `dp[i][j]` represents the side length of the maximum square whose bottom-right corner is at `(i, j)`. If `matrix[i][j] == 1`, `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`. The number of squares ending here is exactly `dp[i][j]`. Sum all `dp[i][j]`.

def countSquares(matrix: List[List[int]]) -> int:
    r, c = len(matrix), len(matrix[0])
    dp = [[0] * c for _ in range(r)]
    ans = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans += dp[i][j]
    return ans

