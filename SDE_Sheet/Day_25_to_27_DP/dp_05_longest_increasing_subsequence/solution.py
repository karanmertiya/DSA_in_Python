# Time Complexity: O(N log N) (Constraint)
# Space Complexity: O(N)
# Explanation: Binary Search Patience Sorting method. Maintain a `temp` array. If current element is larger than `temp.back()`, append. Else, replace the first element >= current.

import bisect
def lengthOfLIS(nums: list[int]) -> int:
    temp = []
    for num in nums:
        idx = bisect.bisect_left(temp, num)
        if idx == len(temp):
            temp.append(num)
        else:
            temp[idx] = num
    return len(temp)

