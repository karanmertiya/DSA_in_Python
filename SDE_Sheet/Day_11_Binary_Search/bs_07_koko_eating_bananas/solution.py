# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
import math
def minEatingSpeed(piles: list[int], h: int) -> int:
    def canEat(k):
        hours = sum(math.ceil(pile / k) for pile in piles)
        return hours <= h
        
    low, high = 1, max(piles)
    ans = high
    while low <= high:
        mid = low + (high - low) // 2
        if canEat(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# Time Complexity: O(N log(Max(P))) (Constraint)
# Space Complexity: O(1)
# Explanation: Optimal: Search space is `1` to `max(piles)`. For a mid `k`, calculate hours required. If `hours <= h`, it's a valid answer, but search left for smaller `k`.

import math
def minEatingSpeed(piles: list[int], h: int) -> int:
    def canEat(k):
        hours = sum(math.ceil(pile / k) for pile in piles)
        return hours <= h
        
    low, high = 1, max(piles)
    ans = high
    while low <= high:
        mid = low + (high - low) // 2
        if canEat(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

