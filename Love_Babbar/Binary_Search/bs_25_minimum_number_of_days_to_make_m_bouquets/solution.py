# Time Complexity: O(N log(Max-Min))
# Space Complexity: O(1)
# Explanation: Binary search on days from `min(bloomDay)` to `max(bloomDay)`. For a given `day`, count consecutive flowers that have bloomed. If count reaches `k`, increment bouquet count and reset flower count. If `bouquets >= m`, move `high = mid - 1`, else `low = mid + 1`.

def minDays(bloomDay: List[int], m: int, k: int) -> int:
    if m * k > len(bloomDay): return -1
    def possible(day):
        count, bouquets = 0, 0
        for bd in bloomDay:
            if bd <= day:
                count += 1
            else:
                bouquets += count // k
                count = 0
        bouquets += count // k
        return bouquets >= m
    low, high = min(bloomDay), max(bloomDay)
    while low <= high:
        mid = low + (high - low) // 2
        if possible(mid): high = mid - 1
        else: low = mid + 1
    return low

