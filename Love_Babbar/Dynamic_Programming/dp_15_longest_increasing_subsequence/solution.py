# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Binary Search approach. Maintain an array `temp` of the increasing sequence. If `nums[i] > temp.back()`, append it. Else, find the lower bound of `nums[i]` in `temp` and replace it.

import bisect
def lengthOfLIS(nums: List[int]) -> int:
    temp = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > temp[-1]: temp.append(nums[i])
        else:
            ind = bisect.bisect_left(temp, nums[i])
            temp[ind] = nums[i]
    return len(temp)

