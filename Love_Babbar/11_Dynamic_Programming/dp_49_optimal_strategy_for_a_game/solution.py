# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: If you pick `i`, opponent picks `i+1` or `j`, leaving you with `(i+2, j)` or `(i+1, j-1)`. Opponent plays optimally to minimize your profit. So you get `A[i] + min(dp(i+2, j), dp(i+1, j-1))`. Similarly for picking `j`. Take the max of these two choices.

def maximumAmount(arr, n):
    dp = [[0] * n for _ in range(n)]
    for gap in range(n):
        for i in range(n - gap):
            j = i + gap
            x = dp[i+2][j] if i + 2 <= j else 0
            y = dp[i+1][j-1] if i + 1 <= j - 1 else 0
            z = dp[i][j-2] if i <= j - 2 else 0
            dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
    return dp[0][n-1]

