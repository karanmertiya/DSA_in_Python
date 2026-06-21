# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Finding exact `k` distinct is hard directly. Instead, find subarrays with at most `k` distinct integers. The number of exact `k` is `atMost(k) - atMost(k - 1)`. The `atMost` function uses a sliding window.

import collections
def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    def atMost(k):
        count = collections.defaultdict(int)
        res = i = 0
        for j in range(len(nums)):
            if count[nums[j]] == 0: k -= 1
            count[nums[j]] += 1
            while k < 0:
                count[nums[i]] -= 1
                if count[nums[i]] == 0: k += 1
                i += 1
            res += j - i + 1
        return res
    return atMost(k) - atMost(k - 1)

