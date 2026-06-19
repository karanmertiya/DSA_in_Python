# Time Complexity: O(N log(Sum-Max))
# Space Complexity: O(1)
# Explanation: Binary search for capacity from `max(weights)` to `sum(weights)`. For a capacity `mid`, calculate days required to ship. If required days <= D, move `high = mid - 1`, else `low = mid + 1`.

def shipWithinDays(weights: List[int], days: int) -> int:
    def find_days(cap):
        d, load = 1, 0
        for weight in weights:
            if load + weight > cap:
                d += 1
                load = weight
            else:
                load += weight
        return d
    low, high = max(weights), sum(weights)
    while low <= high:
        mid = low + (high - low) // 2
        if find_days(mid) <= days: high = mid - 1
        else: low = mid + 1
    return low

