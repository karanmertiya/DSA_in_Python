# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Explanation: Standard MCM DP. `dp[i][j]` is min cost to multiply matrices from `i` to `j`. Iterate length of chain, start `i`, and partition `k`. `dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j])`.

def matrixMultiplication(N: int, arr: List[int]) -> int:
    dp = [[0]*N for _ in range(N)]
    for i in range(N-1, 0, -1):
        for j in range(i+1, N):
            mini = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                mini = min(mini, cost)
            dp[i][j] = mini
    return dp[1][N-1]

