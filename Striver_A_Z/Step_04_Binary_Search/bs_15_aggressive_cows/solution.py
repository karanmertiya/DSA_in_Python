# Time Complexity: O(N log N + N log(Max-Min))
# Space Complexity: O(1)
# Explanation: Sort the stalls. Binary search for distance from `1` to `max-min`. For a distance `mid`, check if we can place all `C` cows such that distance between any two is >= `mid`. If possible, move `low = mid + 1` to maximize it, else `high = mid - 1`.

def aggressiveCows(stalls: List[int], k: int) -> int:
    stalls.sort()
    def can_place(dist):
        cnt_cows = 1
        last = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last >= dist:
                cnt_cows += 1
                last = stalls[i]
        return cnt_cows >= k
    low, high = 1, stalls[-1] - stalls[0]
    while low <= high:
        mid = low + (high - low) // 2
        if can_place(mid): low = mid + 1
        else: high = mid - 1
    return high

