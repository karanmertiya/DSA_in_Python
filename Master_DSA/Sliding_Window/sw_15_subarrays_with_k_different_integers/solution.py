# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Like "Binary Subarrays With Sum", the number of subarrays with exactly k distinct integers is `atMost(k) - atMost(k-1)`. The `atMost` function uses a sliding window with a hash map to track the frequencies of elements.

def subarraysWithKDistinct(nums, k):
    def atMost(limit):
        if limit == 0: return 0
        count = {}
        left, res = 0, 0
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            while len(count) > limit:
                count[nums[left]] -= 1
                if count[nums[left]] == 0: del count[nums[left]]
                left += 1
            res += (right - left + 1)
        return res
    return atMost(k) - atMost(k - 1)

