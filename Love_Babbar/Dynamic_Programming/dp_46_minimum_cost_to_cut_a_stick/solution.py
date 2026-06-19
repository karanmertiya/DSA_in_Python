# Time Complexity: O(C^3) where C is number of cuts
# Space Complexity: O(C^2)
# Explanation: Add 0 and `n` to `cuts`, then sort. `dp[i][j]` is min cost to cut the sub-stick between `cuts[i]` and `cuts[j]`. Try all possible cuts `k` between `i` and `j`. `dp[i][j] = min(dp[i][k] + dp[k][j]) + cuts[j] - cuts[i]`.

def minCost(n: int, cuts: List[int]) -> int:
    cuts = [0] + sorted(cuts) + [n]
    c = len(cuts)
    dp = [[0] * c for _ in range(c)]
    for length in range(2, c):
        for i in range(c - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
    return dp[0][c-1]

