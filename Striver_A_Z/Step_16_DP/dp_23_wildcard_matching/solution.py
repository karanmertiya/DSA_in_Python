# Time Complexity: O(N * M)
# Space Complexity: O(N * M) or O(M)
# Explanation: Use a 2D DP array where `dp[i][j]` means if `s[0..i-1]` matches `p[0..j-1]`. If `p[j-1] == '?'` or `s[i-1] == p[j-1]`, `dp[i][j] = dp[i-1][j-1]`. If `p[j-1] == '*'`, it can match empty (`dp[i][j-1]`) or match one character (`dp[i-1][j]`).

def isMatch(s: str, p: str) -> bool:
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for j in range(1, m + 1):
        if p[j-1] == '*': dp[0][j] = dp[0][j-1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j-1] in {s[i-1], '?'}:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    return dp[n][m]

