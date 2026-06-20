# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Find the Longest Palindromic Subsequence (LPS). The minimum insertions required will be `string_length - LPS_length`. LPS is just LCS(s, reverse(s)).

def minInsertions(s):
    n = len(s)
    t = s[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return n - dp[n][n]

