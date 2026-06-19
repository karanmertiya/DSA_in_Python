# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: If `s[i] == s[j]`, `dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1`. If `s[i] != s[j]`, `dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]`.

def countPS(string: str) -> int:
    n = len(string)
    mod = 10**9 + 7
    dp = [[0] * n for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if string[i] == string[j]:
                dp[i][j] = (dp[i+1][j] + dp[i][j-1] + 1) % mod
            else:
                dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % mod
    return dp[0][n-1]

