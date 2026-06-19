# Time Complexity: O(N * M)
# Space Complexity: O(M)
# Explanation: If chars match, move both pointers. Else, try all 3 ops: 1 + min(insert(i, j-1), delete(i-1, j), replace(i-1, j-1)). Space optimized to 1D.

def minDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        cur = [0] * (m + 1)
        cur[0] = i
        for j in range(1, m + 1):
            if word1[i-1] == word2[j-1]: cur[j] = prev[j-1]
            else: cur[j] = 1 + min(prev[j-1], prev[j], cur[j-1])
        prev = cur
    return prev[m]

