# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Use DP. `dp[i][j]` stores the count of palindromic subsequences in `str[i..j]`. If `str[i] == str[j]`, `dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1`. Else, `dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]`.

def countPS(str_val):
    MOD = 10**9 + 7
    n = len(str_val)
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if str_val[i] == str_val[j]:
                dp[i][j] = (dp[i+1][j] + dp[i][j-1] + 1) % MOD
            else:
                dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % MOD
    return dp[0][n - 1]

