# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: 1. Find the largest index k such that nums[k] < nums[k + 1]. 2. Find the largest index l greater than k such that nums[k] < nums[l]. 3. Swap nums[k] and nums[l]. 4. Reverse the sub-array nums[k + 1:].

def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    k = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            k = i; break
    if k < 0: nums.reverse(); return
    for i in range(n - 1, k, -1):
        if nums[i] > nums[k]:
            nums[k], nums[i] = nums[i], nums[k]
            break
    nums[k + 1:] = reversed(nums[k + 1:])

