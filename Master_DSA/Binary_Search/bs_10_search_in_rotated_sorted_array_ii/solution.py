# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def search(nums: List[int], target: int) -> bool:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1; high -= 1; continue
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]: high = mid - 1
            else: low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]: low = mid + 1
            else: high = mid - 1
    return False

# Time Complexity: O(log N) average, O(N) worst case
# Space Complexity: O(1)
# Explanation: Optimal: If `nums[low] == nums[mid] == nums[high]`, shrink the search space by `low++` and `high--`. Otherwise, proceed with the standard rotated binary search.

def search(nums: List[int], target: int) -> bool:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1; high -= 1; continue
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]: high = mid - 1
            else: low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]: low = mid + 1
            else: high = mid - 1
    return False

