# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# Explanation: DP state `dp[i][j]` is true if `s[0..i-1]` matches `p[0..j-1]`. Base cases: empty pattern only matches empty string. `p[0..j-1]` can match empty string if all chars are '*'. Transitions: If `s[i-1] == p[j-1]` or `p[j-1] == '?'`, `dp[i][j] = dp[i-1][j-1]`. If `p[j-1] == '*'`, it can match empty string (`dp[i][j-1]`) or one/more characters (`dp[i-1][j]`).

def isMatch(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j-1] == '*': dp[0][j] = dp[0][j-1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '?' or s[i-1] == p[j-1]: dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*': dp[i][j] = dp[i-1][j] or dp[i][j-1]
    return dp[m][n]

