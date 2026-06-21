# Time Complexity: O(log N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Standard Iterative approach. Maintain `low` and `high` boundaries, shrinking the search space by half.

def search(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

