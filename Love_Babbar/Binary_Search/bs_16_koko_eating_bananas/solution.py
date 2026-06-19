# Time Complexity: O(N log(max(P)))
# Space Complexity: O(1)
# Explanation: Binary search on the answer. Minimum speed is 1, maximum is `max(piles)`. For a given speed `mid`, calculate total hours `sum(ceil(pile / mid))`. If `<= h`, search lower half.

import math
def minEatingSpeed(piles: List[int], h: int) -> int:
    low, high = 1, max(piles)
    while low <= high:
        mid = (low + high) // 2
        total = sum(math.ceil(p / mid) for p in piles)
        if total <= h: high = mid - 1
        else: low = mid + 1
    return low

