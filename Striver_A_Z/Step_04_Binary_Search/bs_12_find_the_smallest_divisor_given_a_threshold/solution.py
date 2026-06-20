# Time Complexity: O(N log(max(nums)))
# Space Complexity: O(1)
# Explanation: Optimal: Binary search the divisor from 1 to `max(nums)`. Compute `sum(ceil(num / mid))`. If sum <= threshold, shrink high.

import math
def smallestDivisor(nums: List[int], threshold: int) -> int:
    low, high = 1, max(nums)
    while low <= high:
        mid = (low + high) // 2
        total = sum(math.ceil(num / mid) for num in nums)
        if total <= threshold: high = mid - 1
        else: low = mid + 1
    return low

