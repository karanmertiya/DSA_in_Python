# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Maintain a Hash Map of `prefix_sum` -> `frequency`. If `curr_sum - k` exists in the map, add its frequency to the count.

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

