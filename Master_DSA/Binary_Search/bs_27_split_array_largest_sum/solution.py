# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
# Explanation: Search space is `[max(nums), sum(nums)]`. For a `mid` maximum sum, count the subarrays needed. If `count <= k`, `mid` is possible, search left. Else, search right. This is identical to the Painter's Partition or Book Allocation problem.

def splitArray(nums, k):
    def countSubarrays(maxSum):
        partitions, currentSum = 1, 0
        for num in nums:
            if currentSum + num <= maxSum:
                currentSum += num
            else:
                partitions += 1
                currentSum = num
        return partitions
    low, high = max(nums), sum(nums)
    while low <= high:
        mid = (low + high) // 2
        if countSubarrays(mid) > k: low = mid + 1
        else: high = mid - 1
    return low

