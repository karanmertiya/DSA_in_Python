# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Brute Force: Use any standard sorting algorithm like Merge Sort.

def sortColors(nums):
    nums.sort()

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Dutch National Flag Algorithm (3 pointers). `low` tracks 0s, `mid` scans array, `high` tracks 2s. Swap elements to maintain sections.

def sortColors(nums: list[int]) -> None:
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

