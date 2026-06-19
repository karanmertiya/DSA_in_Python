# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Find first dip from right (i). Find element just larger than nums[i] from right (j). Swap them and reverse the array from i+1 to end.

def nextPermutation(nums: List[int]) -> None:
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]: i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]: j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = reversed(nums[i+1:])

