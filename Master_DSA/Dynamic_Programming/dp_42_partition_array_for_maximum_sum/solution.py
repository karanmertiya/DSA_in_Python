# Time Complexity: O(N * K)
# Space Complexity: O(N)
# Explanation: Let `dp[i]` be the maximum sum for `arr[0..i-1]`. To compute `dp[i]`, iterate back `j` from 1 to `k`. Keep track of the maximum element in `arr[i-j..i-1]`. The sum is `max_val * j + dp[i-j]`. Maximize this over all valid `j`.

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        cur_max = 0
        best = 0
        for j in range(1, min(k, i) + 1):
            cur_max = max(cur_max, arr[i-j])
            best = max(best, dp[i-j] + cur_max * j)
        dp[i] = best
    return dp[n]

