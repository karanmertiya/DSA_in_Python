# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Two-pointer approach. Swap non-zero elements with the `zero_pointer`.

def move_zeroes(nums: list[int]) -> None:
    zero_idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
            zero_idx += 1

