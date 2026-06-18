# Time Complexity: O(N log(Max(Pile))) (Constraint)
# Space Complexity: O(1)
# Explanation: Search space is `1` to `max(piles)`. Calculate total hours for `mid`. If possible, try a slower speed (left half).

import math
def min_eating_speed(piles: list[int], h: int) -> int:
    def can_eat(speed):
        hours = 0
        for p in piles:
            hours += math.ceil(p / speed)
        return hours <= h
        
    low, high = 1, max(piles)
    ans = high
    while low <= high:
        mid = low + (high - low) // 2
        if can_eat(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

