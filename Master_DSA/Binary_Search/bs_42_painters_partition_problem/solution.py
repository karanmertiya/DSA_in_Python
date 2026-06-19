# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
# Explanation: Similar to Book Allocation. Find if it's possible to paint all boards within `mid` time using at most `K` painters. Search space from `max(arr)` to `sum(arr)`.

def minTime(arr: List[int], n: int, k: int) -> int:
    def isPossible(mid):
        painters, curr_sum = 1, 0
        for x in arr:
            if curr_sum + x > mid:
                painters += 1
                curr_sum = x
                if painters > k or x > mid: return False
            else:
                curr_sum += x
        return True
    low, high = max(arr), sum(arr)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

