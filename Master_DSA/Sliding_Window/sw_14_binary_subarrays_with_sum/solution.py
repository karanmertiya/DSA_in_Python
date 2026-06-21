# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use the helper function `atMost(goal)` which finds the number of subarrays with sum <= goal. The answer is `atMost(goal) - atMost(goal - 1)`. In `atMost`, use a sliding window to maintain the sum.

def numSubarraysWithSum(nums, goal):
    def atMost(k):
        if k < 0: return 0
        left, sum_val, count = 0, 0, 0
        for right in range(len(nums)):
            sum_val += nums[right]
            while sum_val > k:
                sum_val -= nums[left]
                left += 1
            count += (right - left + 1)
        return count
    return atMost(goal) - atMost(goal - 1)

