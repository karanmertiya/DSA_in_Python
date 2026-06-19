# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Maintain an array `tails` where `tails[i]` stores the smallest tail of all increasing subsequences of length `i+1`. Use binary search (`lower_bound`) to find the position to replace or append.

import bisect
def lengthOfLIS(nums: List[int]) -> int:
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails): tails.append(num)
        else: tails[idx] = num
    return len(tails)

