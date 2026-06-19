# Time Complexity: O(N log(max_day))
# Space Complexity: O(1)
# Explanation: If `m * k > n`, return -1. Binary search on days `[min(bloomDay), max(bloomDay)]`. For a given day, count adjacent bloomed flowers. Every `k` consecutive bloomed flowers make 1 bouquet. If total bouquets >= m, search left. Else search right.

def minDays(bloomDay: List[int], m: int, k: int) -> int:
    if m * k > len(bloomDay): return -1
    low, high = min(bloomDay), max(bloomDay)
    while low <= high:
        mid = low + (high - low) // 2
        bouquets, count = 0, 0
        for day in bloomDay:
            if day <= mid:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
        if bouquets >= m:
            high = mid - 1
        else:
            low = mid + 1
    return low

