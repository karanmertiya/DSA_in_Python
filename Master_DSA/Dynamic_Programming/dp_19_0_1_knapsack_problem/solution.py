# Time Complexity: O(N * W)
# Space Complexity: O(W)
# Explanation: Use a 1D `dp` array of size `W + 1`. For each item, iterate backwards from `W` to `weight[i]`. `dp[w] = max(dp[w], val[i] + dp[w - weight[i]])`.

def knapSack(W: int, wt: List[int], val: List[int], n: int) -> int:
    dp = [0] * (W + 1)
    for i in range(n):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
    return dp[W]

