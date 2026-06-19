# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Front Partitioning. `dp[i]` is the minimum cuts for `s[i...n-1]`. To compute `dp[i]`, iterate `j` from `i` to `n-1`. If `s[i...j]` is a palindrome, then `cost = 1 + dp[j+1]`. `dp[i]` is the minimum of these costs. Return `dp[0] - 1`.

def minCut(s: str) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        min_cuts = float('inf')
        for j in range(i, n):
            if s[i:j+1] == s[i:j+1][::-1]:
                cost = 1 + dp[j+1]
                min_cuts = min(min_cuts, cost)
        dp[i] = min_cuts
    return dp[0] - 1

