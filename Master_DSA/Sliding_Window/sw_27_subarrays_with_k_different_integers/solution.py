# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Exact K = At Most K - At Most K-1. Use a helper function `atMost(nums, k)` that uses a sliding window to count subarrays with at most `k` distinct integers.

def subarraysWithKDistinct(nums, k):
    def atMost(k):
        m = {}
        left, count = 0, 0
        for right in range(len(nums)):
            if m.get(nums[right], 0) == 0: k -= 1
            m[nums[right]] = m.get(nums[right], 0) + 1
            while k < 0:
                m[nums[left]] -= 1
                if m[nums[left]] == 0: k += 1
                left += 1
            count += right - left + 1
        return count
    return atMost(k) - atMost(k - 1)

