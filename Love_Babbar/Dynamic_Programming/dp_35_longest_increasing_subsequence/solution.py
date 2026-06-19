# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Maintain an array `temp` storing the smallest tail of all increasing subsequences of length i+1 in `temp[i]`. For each num, use binary search to find its position in `temp`. If num is larger than all, append it. Otherwise, replace the element.

import bisect
def lengthOfLIS(nums):
    temp = []
    for num in nums:
        idx = bisect.bisect_left(temp, num)
        if idx == len(temp): temp.append(num)
        else: temp[idx] = num
    return len(temp)

