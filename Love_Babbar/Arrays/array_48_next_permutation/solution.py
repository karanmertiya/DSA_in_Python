# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: 1. Find largest index `k` such that `nums[k] < nums[k + 1]`. If no such index exists, the permutation is the last permutation, reverse it. 2. Find the largest index `l` greater than `k` such that `nums[k] < nums[l]`. 3. Swap `nums[k]` and `nums[l]`. 4. Reverse the sub-array `nums[k + 1:]`.

def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    k = n - 2
    while k >= 0 and nums[k] >= nums[k + 1]:
        k -= 1
    if k < 0:
        nums.reverse()
        return
    l = n - 1
    while l > k and nums[l] <= nums[k]:
        l -= 1
    nums[k], nums[l] = nums[l], nums[k]
    nums[k+1:] = reversed(nums[k+1:])

