# Time Complexity: O(N log(max-min))
# Space Complexity: O(1)
# Explanation: If `m * k > n`, return -1. Search space for days is `[min(bloomDay), max(bloomDay)]`. For a `mid` day, count consecutive flowers that have bloomed (`bloomDay[i] <= mid`). If consecutive count reaches `k`, increment bouquet count. If `bouquets >= m`, move `high = mid - 1`, else `low = mid + 1`.

def minDays(bloomDay, m, k):
    n = len(bloomDay)
    if m * k > n: return -1
    def possible(day):
        cnt = 0
        noOfB = 0
        for bd in bloomDay:
            if bd <= day: cnt += 1
            else:
                noOfB += cnt // k
                cnt = 0
        noOfB += cnt // k
        return noOfB >= m
    low, high = min(bloomDay), max(bloomDay)
    while low <= high:
        mid = (low + high) // 2
        if possible(mid): high = mid - 1
        else: low = mid + 1
    return low

