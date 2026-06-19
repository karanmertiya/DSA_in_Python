# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a sliding window. Add elements to the current sum. While the sum is >= target, update the minimum length and shrink the window from the left.

def minSubArrayLen(target: int, nums: List[int]) -> int:
    l = sum = 0
    minLen = float('inf')
    for r in range(len(nums)):
        sum += nums[r]
        while sum >= target:
            minLen = min(minLen, r - l + 1)
            sum -= nums[l]
            l += 1
    return 0 if minLen == float('inf') else minLen

