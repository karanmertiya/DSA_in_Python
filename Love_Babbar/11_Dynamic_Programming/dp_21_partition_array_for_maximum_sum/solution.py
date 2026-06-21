# Time Complexity: O(N * K)
# Space Complexity: O(N)
# Explanation: Front partitioning. `dp[i]` is max sum for `arr[i..n-1]`. For each `i`, iterate `j` up to `i+k-1`. Find `maxi` element in this window, and add `maxi * length + dp[j+1]`.

def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        max_val = 0
        max_ans = 0
        length = 0
        for j in range(i, min(n, i + k)):
            length += 1
            max_val = max(max_val, arr[j])
            current_sum = max_val * length + dp[j+1]
            max_ans = max(max_ans, current_sum)
        dp[i] = max_ans
    return dp[0]

