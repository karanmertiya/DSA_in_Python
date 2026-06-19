# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a sliding window. Add elements to `sum`. While `sum >= target`, update `min_len` and subtract `nums[left]` from `sum`, incrementing `left`.

def minSubArrayLen(target, nums):
    left, minLen, sum_val = 0, float('inf'), 0
    for right in range(len(nums)):
        sum_val += nums[right]
        while sum_val >= target:
            minLen = min(minLen, right - left + 1)
            sum_val -= nums[left]
            left += 1
    return 0 if minLen == float('inf') else minLen

