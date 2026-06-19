# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
# Explanation: Binary search on capacity `[max(weights), sum(weights)]`. For a `mid` capacity, greedily load packages. If a package makes sum > capacity, increment days and start new load. If `days <= D`, search left. Else search right.

def shipWithinDays(weights: List[int], days: int) -> int:
    low, high = max(weights), sum(weights)
    while low <= high:
        mid = low + (high - low) // 2
        d, load = 1, 0
        for w in weights:
            if load + w > mid:
                d += 1
                load = w
            else:
                load += w
        if d <= days:
            high = mid - 1
        else:
            low = mid + 1
    return low

