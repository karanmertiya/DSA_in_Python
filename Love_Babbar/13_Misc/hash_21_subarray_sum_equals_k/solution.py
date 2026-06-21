# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Explanation: Brute Force: Generate all possible subarrays and compute their sums.

def subarraySum(nums, k):
    count = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    return count

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Optimal: Maintain a Hash Map of `prefix_sum` -> `frequency`. If `curr_sum - k` exists in the map, add its frequency to the count.

def subarray_sum(nums: list[int], k: int) -> int:
    prefix_freq = {0: 1}
    count = 0
    curr_sum = 0
    for num in nums:
        curr_sum += num
        remove = curr_sum - k
        if remove in prefix_freq:
            count += prefix_freq[remove]
        prefix_freq[curr_sum] = prefix_freq.get(curr_sum, 0) + 1
    return count

