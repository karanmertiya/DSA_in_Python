# Time Complexity: O(N log(max))
# Space Complexity: O(1)
# Explanation: Search space for divisor is `[1, max(nums)]`. For a `mid` divisor, compute the sum of `ceil(nums[i] / mid)`. If sum is `<= threshold`, search left (`high = mid - 1`). Else, search right.

import math
def smallestDivisor(nums, threshold):
    def sumByD(div):
        return sum(math.ceil(num / div) for num in nums)
    low, high = 1, max(nums)
    while low <= high:
        mid = (low + high) // 2
        if sumByD(mid) <= threshold: high = mid - 1
        else: low = mid + 1
    return low

