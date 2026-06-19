# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Use lower_bound for the first occurrence. Use upper_bound - 1 for the last occurrence. Validate if the target actually exists at the lower_bound index.

import bisect
def searchRange(nums: List[int], target: int) -> List[int]:
    lb = bisect.bisect_left(nums, target)
    ub = bisect.bisect_right(nums, target)
    if lb == len(nums) or nums[lb] != target: return [-1, -1]
    return [lb, ub - 1]

