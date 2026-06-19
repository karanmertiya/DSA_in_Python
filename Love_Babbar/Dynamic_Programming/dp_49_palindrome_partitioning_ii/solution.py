# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Precompute a 2D boolean array `isPal` indicating if `s[i..j]` is palindrome. Then use 1D DP `cuts[i]` indicating min cuts for `s[0..i]`. `cuts[i] = min(cuts[i], cuts[j-1] + 1)` for all `j <= i` where `isPal[j][i]` is true. If `isPal[0][i]` is true, `cuts[i] = 0`.

def minCut(s: str) -> int:
    n = len(s)
    isPal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i <= 2 or isPal[i+1][j-1]):
                isPal[i][j] = True
    cuts = [0] * n
    for i in range(n):
        if isPal[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = i
            for j in range(1, i + 1):
                if isPal[j][i]:
                    cuts[i] = min(cuts[i], cuts[j-1] + 1)
    return cuts[n-1]

