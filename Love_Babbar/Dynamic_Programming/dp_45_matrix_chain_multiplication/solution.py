# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Explanation: Use DP where `dp[i][j]` is min cost to multiply matrices from `i` to `j`. `dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j])` for all `i <= k < j`. Solve for subproblem lengths 2 to N.

def matrixMultiplication(N, arr):
    dp = [[0] * N for _ in range(N)]
    for length in range(2, N):
        for i in range(1, N - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)
    return dp[1][N-1]

