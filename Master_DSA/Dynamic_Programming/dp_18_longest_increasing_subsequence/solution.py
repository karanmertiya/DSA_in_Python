# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Create a `dp` array of size `n` initialized to 1. For each `i` from 1 to `n-1`, check all `j` from 0 to `i-1`. If `nums[i] > nums[j]`, update `dp[i] = max(dp[i], dp[j] + 1)`. The result is the max in `dp`.

def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

