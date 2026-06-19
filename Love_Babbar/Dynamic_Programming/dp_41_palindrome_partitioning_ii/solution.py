# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: First, precompute a 2D boolean array `isPal[i][j]` to quickly check if `s[i..j]` is a palindrome. Then, use a 1D DP array where `dp[i]` represents the minimum cuts for `s[0..i]`. For each `i`, iterate `j` from `0` to `i`. If `s[j..i]` is a palindrome, then `dp[i] = min(dp[i], dp[j-1] + 1)`. If `s[0..i]` is a palindrome, `dp[i] = 0`.

def minCut(s):
    n = len(s)
    isPal = [[False] * n for _ in range(n)]
    for i in range(n):
        isPal[i][i] = True
        if i < n - 1 and s[i] == s[i+1]: isPal[i][i+1] = True
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and isPal[i+1][j-1]: isPal[i][j] = True
    dp = [0] * n
    for i in range(n):
        if isPal[0][i]:
            dp[i] = 0
            continue
        min_cuts = i
        for j in range(1, i + 1):
            if isPal[j][i]: min_cuts = min(min_cuts, dp[j-1] + 1)
        dp[i] = min_cuts
    return dp[n-1]

