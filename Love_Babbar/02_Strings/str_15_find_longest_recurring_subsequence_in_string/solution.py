# Time Complexity: O(N^2)
# Space Complexity: O(N^2) or O(N)
# Explanation: This is a variation of Longest Common Subsequence (LCS). Find LCS of `str` with itself, but with the restriction that when characters match, their indices must not be the same (`i != j`).

def LongestRepeatingSubsequence(str: str) -> int:
    n = len(str)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str[i-1] == str[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][n]

