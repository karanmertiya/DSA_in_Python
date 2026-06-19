# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
# Explanation: If total sum is odd, it's impossible. Otherwise, target is `sum / 2`. The problem reduces to subset sum. Use a boolean `dp` array of size `target + 1`. `dp[j] = dp[j] || dp[j - num]`.

def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0: return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]

