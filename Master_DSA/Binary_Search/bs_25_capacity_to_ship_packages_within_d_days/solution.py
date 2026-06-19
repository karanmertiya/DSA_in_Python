# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
# Explanation: Search space is `[max(weights), sum(weights)]`. For a `mid` capacity, simulate loading the ship. If day count exceeds `days`, capacity is too small (`low = mid + 1`). Otherwise, try for a smaller capacity (`high = mid - 1`).

def shipWithinDays(weights, days):
    def findDays(cap):
        d, load = 1, 0
        for w in weights:
            if load + w > cap:
                d += 1
                load = w
            else:
                load += w
        return d
    low, high = max(weights), sum(weights)
    while low <= high:
        mid = (low + high) // 2
        if findDays(mid) <= days: high = mid - 1
        else: low = mid + 1
    return low

