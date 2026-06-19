# Time Complexity: O(N * K)
# Space Complexity: O(N * K)
# Explanation: Use a 2D DP array where `dp[i][j]` is the number of subsequences of first `i` elements with product less than or equal to `j`. `dp[i][j] = dp[i-1][j] + dp[i-1][j/arr[i-1]] + 1`.

def countSubsequences(a, k):
    n = len(a)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] <= j and a[i - 1] > 0:
                dp[i][j] += dp[i - 1][j // a[i - 1]] + 1
    return dp[n][k]

