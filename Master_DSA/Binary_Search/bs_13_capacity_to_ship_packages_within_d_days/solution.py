# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
# Explanation: Binary search on capacity. Low = `max(weights)`, High = `sum(weights)`. Iterate through packages and accumulate weight, increment day if limit is exceeded.

def shipWithinDays(weights: List[int], days: int) -> int:
    def canShip(cap):
        d, load = 1, 0
        for w in weights:
            if load + w > cap: d += 1; load = w
            else: load += w
        return d <= days
    low, high = max(weights), sum(weights)
    while low <= high:
        mid = (low + high) // 2
        if canShip(mid): high = mid - 1
        else: low = mid + 1
    return low

