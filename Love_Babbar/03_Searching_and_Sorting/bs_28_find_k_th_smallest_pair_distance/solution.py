# Time Complexity: O(N log N + N log(max_dist))
# Space Complexity: O(1)
# Explanation: Optimal: Sort array. Binary search on distance `[0, nums.back() - nums.front()]`. For a candidate `mid`, count pairs with distance `<= mid` using a sliding window. If count >= k, search left. Else search right.

def smallestDistancePair(nums: List[int], k: int) -> int:
    nums.sort()
    low, high = 0, nums[-1] - nums[0]
    def countPairs(mid):
        count, l = 0, 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > mid: l += 1
            count += (r - l)
        return count
    while low < high:
        mid = low + (high - low) // 2
        if countPairs(mid) >= k:
            high = mid
        else:
            low = mid + 1
    return low

