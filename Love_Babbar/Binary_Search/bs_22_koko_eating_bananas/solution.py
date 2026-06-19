# Time Complexity: O(N log(max(piles)))
# Space Complexity: O(1)
# Explanation: Search space for speed `k` is `[1, max(piles)]`. For a chosen `mid` speed, calculate the total hours needed. If `total_hours <= h`, this `mid` is a possible answer, search left for smaller speed. Else search right.

import math
def minEatingSpeed(piles, h):
    def calculateTotalHours(hourly):
        return sum(math.ceil(p / hourly) for p in piles)
    low, high = 1, max(piles)
    while low <= high:
        mid = (low + high) // 2
        if calculateTotalHours(mid) <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

