# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
# Explanation: Subset sum variation. `S1 - S2 = target`, `S1 + S2 = totalSum`. So, `S1 = (target + totalSum) / 2`. Find subsets with this target sum.

def findTargetSumWays(nums: List[int], target: int) -> int:
    total = sum(nums)
    if total - target < 0 or (total - target) % 2 == 1: return 0
    s2 = (total - target) // 2
    prev = [0] * (s2 + 1)
    if nums[0] == 0: prev[0] = 2
    else: prev[0] = 1
    if nums[0] != 0 and nums[0] <= s2: prev[nums[0]] = 1
    for ind in range(1, len(nums)):
        cur = [0] * (s2 + 1)
        for t in range(s2 + 1):
            notTaken = prev[t]
            taken = 0
            if nums[ind] <= t: taken = prev[t - nums[ind]]
            cur[t] = notTaken + taken
        prev = cur
    return prev[s2]

