# Time Complexity: O(N log(Sum-Max))
# Space Complexity: O(1)
# Explanation: Optimal: Identical logic to Allocate Books. Binary search from `max(nums)` to `sum(nums)`.

def splitArray(nums: List[int], k: int) -> int:
    def count_partitions(max_sum):
        partitions, subarray_sum = 1, 0
        for num in nums:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        return partitions
    low, high = max(nums), sum(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if count_partitions(mid) > k: low = mid + 1
        else: high = mid - 1
    return low

