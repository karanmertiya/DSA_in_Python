# Time Complexity: O(N log(Max))
# Space Complexity: O(1)
# Explanation: Binary search for divisor from `1` to `max(nums)`. For a divisor `mid`, sum `ceil(num / mid)`. If sum <= threshold, move `high = mid - 1`, else `low = mid + 1`.

import math
def smallestDivisor(nums: List[int], threshold: int) -> int:
    def sum_by_d(d):
        return sum(math.ceil(num / d) for num in nums)
    low, high = 1, max(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if sum_by_d(mid) <= threshold: high = mid - 1
        else: low = mid + 1
    return low

