# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Create a dp array where dp[i] is the length of LIS ending at index i. For each i, check all j < i to see if nums[i] > nums[j] and update dp[i] = max(dp[i], dp[j] + 1). O(N log N) patience sorting approach is better but standard DP is O(N^2).

def lengthOfLIS(nums: List[int]) -> int:
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

