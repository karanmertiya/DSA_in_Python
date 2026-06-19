# Time Complexity: O(N log N + N log(max_val))
# Space Complexity: O(1)
# Explanation: Sort array. Maximize the minimum distance. Search space from `1` to `max(arr) - min(arr)`. Function `isPossible(mid)` checks if we can place `K` cows such that distance between any two is at least `mid`.

def solve(n: int, k: int, stalls: List[int]) -> int:
    stalls.sort()
    def isPossible(mid):
        cows, lastPos = 1, stalls[0]
        for i in range(1, n):
            if stalls[i] - lastPos >= mid:
                cows += 1
                lastPos = stalls[i]
                if cows == k: return True
        return False
    low, high = 1, stalls[-1] - stalls[0]
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

