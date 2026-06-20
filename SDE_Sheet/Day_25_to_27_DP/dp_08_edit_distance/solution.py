# Time Complexity: O(N * M)
# Space Complexity: O(M)
# Explanation: 2D DP. If chars match, dp[i-1][j-1]. Else, 1 + min(insert, delete, replace).

def minDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    prev = list(range(m+1))
    for i in range(1, n+1):
        cur = [i] + [0]*m
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]: cur[j] = prev[j-1]
            else: cur[j] = 1 + min(prev[j], cur[j-1], prev[j-1])
        prev = cur
    return prev[m]

