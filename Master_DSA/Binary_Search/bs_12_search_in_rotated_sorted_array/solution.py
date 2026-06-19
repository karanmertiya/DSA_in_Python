# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Binary Search. Identify which half is sorted. If left half is sorted and target is in its range, move `high = mid - 1`, else `low = mid + 1`. Symmetrically for right half.

def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target: return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]: high = mid - 1
            else: low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]: low = mid + 1
            else: high = mid - 1
    return -1

