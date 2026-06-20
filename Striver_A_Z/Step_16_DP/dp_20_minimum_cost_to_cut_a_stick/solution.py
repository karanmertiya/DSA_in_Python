# Time Complexity: O(C^3) where C is number of cuts
# Space Complexity: O(C^2)
# Explanation: Sort cuts array and prepend 0, append `n`. Use MCM pattern. `dp[i][j]` is the minimum cost to cut the stick between cuts `i` and `j`. `dp[i][j] = min(cost + cuts[j+1] - cuts[i-1])`.

def minCost(n: int, cuts: List[int]) -> int:
    cuts = [0] + sorted(cuts) + [n]
    c = len(cuts) - 2
    dp = [[0] * (c + 2) for _ in range(c + 2)]
    for i in range(c, 0, -1):
        for j in range(1, c + 1):
            if i > j: continue
            mini = float('inf')
            for k in range(i, j + 1):
                cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
                mini = min(mini, cost)
            dp[i][j] = mini
    return dp[1][c]

