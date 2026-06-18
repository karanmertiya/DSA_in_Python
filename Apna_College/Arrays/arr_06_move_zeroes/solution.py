# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Two-pointer approach (Snowball method). Pointer `i` tracks the first zero found, pointer `j` scans for non-zeroes to swap.

def moveZeroes(nums: list[int]) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

