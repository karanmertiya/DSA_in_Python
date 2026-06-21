# Time Complexity: O(L * log(max_time))
# Space Complexity: O(1)
# Explanation: Optimal: Search space is `0` to `max_time`, where `max_time` is the time taken by the fastest cook to make all `P` pratas alone. `isPossible(mid)` checks if the total pratas made by all cooks in `mid` time is at least `P`.

def minTime(p: int, rank: List[int]) -> int:
    def isPossible(mid):
        count = 0
        for r in rank:
            time, j = 0, 1
            while time + r * j <= mid:
                count += 1
                time += r * j
                j += 1
            if count >= p: return True
        return count >= p
    low, high = 0, 10**8
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

