# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
# Explanation: If total sum is odd, impossible. Else, find if there's a subset with sum `Total/2` using space-optimized DP.

def canPartition(nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0: return False
    target = total_sum // 2
    prev = [False] * (target + 1)
    prev[0] = True
    if nums[0] <= target: prev[nums[0]] = True
    for ind in range(1, len(nums)):
        cur = [False] * (target + 1)
        cur[0] = True
        for t in range(1, target + 1):
            notTaken = prev[t]
            taken = False
            if nums[ind] <= t: taken = prev[t - nums[ind]]
            cur[t] = notTaken or taken
        prev = cur
    return prev[target]

