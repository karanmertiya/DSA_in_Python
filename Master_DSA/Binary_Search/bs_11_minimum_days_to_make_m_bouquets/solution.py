# Time Complexity: O(N log(maxD - minD))
# Space Complexity: O(1)
# Explanation: Binary search on days from `min(bloom)` to `max(bloom)`. Count consecutive bloomed flowers, if it reaches `k`, form a bouquet. Return minimum valid day.

def minDays(bloomDay: List[int], m: int, k: int) -> int:
    if m * k > len(bloomDay): return -1
    def isPossible(day):
        count, bouquets = 0, 0
        for d in bloomDay:
            if d <= day: count += 1
            else: bouquets += count // k; count = 0
        bouquets += count // k
        return bouquets >= m
    low, high = min(bloomDay), max(bloomDay)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid): ans = mid; high = mid - 1
        else: low = mid + 1
    return ans

