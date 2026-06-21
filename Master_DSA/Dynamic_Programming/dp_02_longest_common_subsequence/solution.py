# Time Complexity: O(M * N) (Constraint)
# Space Complexity: O(M * N) (Trade-off)
# Explanation: Tabulation (Bottom-Up). Use a 2D array where `dp[i][j]` represents the LCS of prefixes of length `i` and `j`.

def longestCommonSubsequence(text1: str, text2: str) -> int:
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

