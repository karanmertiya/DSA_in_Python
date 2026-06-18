# Time Complexity: O(2N) &cong; O(N) (Trade-off)
# Space Complexity: O(1)
# Explanation: Count 0s, 1s, and 2s, then overwrite the array linearly.

def sort_colors_better(nums: list[int]) -> None:
    c0 = c1 = c2 = 0
    for num in nums:
        if num == 0: c0 += 1
        elif num == 1: c1 += 1
        else: c2 += 1
    for i in range(c0): nums[i] = 0
    for i in range(c0, c0+c1): nums[i] = 1
    for i in range(c0+c1, len(nums)): nums[i] = 2

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Dutch National Flag Algorithm: 3 Pointers (low, mid, high) sorting in a single pass.

def sort_colors_optimal(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

