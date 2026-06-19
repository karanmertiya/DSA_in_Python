# Time Complexity: O(N * K)
# Space Complexity: O(N)
# Explanation: `dp[i]` is max sum for prefix of length `i`. To find `dp[i]`, try all partition lengths `j` from 1 to `k`. Keep track of `max_val` in the last `j` elements. `dp[i] = max(dp[i], dp[i-j] + max_val * j)`.

def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, min(k, i) + 1):
            max_val = max(max_val, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_val * j)
    return dp[n]

