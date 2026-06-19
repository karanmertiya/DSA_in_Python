# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Explanation: Add 1 to both ends of the array. Let `dp[i][j]` be the max coins collected by bursting balloons in `nums[i..j]`. Iterate length `L` from 1 to N. For each window `[i, j]`, try every `k` from `i` to `j` as the LAST balloon to burst in this window. Cost is `nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]`.

def maxCoins(nums):
    n = len(nums)
    arr = [1] + nums + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for L in range(1, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            for k in range(i, j + 1):
                cost = arr[i-1] * arr[k] * arr[j+1] + dp[i][k-1] + dp[k+1][j]
                dp[i][j] = max(dp[i][j], cost)
    return dp[1][n]

