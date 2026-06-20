# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Replace all odd numbers with 1 and even numbers with 0. The problem then reduces to finding the number of subarrays with a sum equal to k. Use the `atMost(k) - atMost(k - 1)` sliding window approach.

def numberOfSubarrays(nums, k):
    def atMost(limit):
        if limit < 0: return 0
        left, count, res = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0: count += 1
            while count > limit:
                if nums[left] % 2 != 0: count -= 1
                left += 1
            res += (right - left + 1)
        return res
    return atMost(k) - atMost(k - 1)

