# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Find which half is sorted. If left half is sorted, check if target lies in it. If yes, search left, else search right. If right half is sorted, check if target lies in it. If yes, search right, else search left.

def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target: return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]: high = mid - 1
            else: low = mid + 1
        else:
            if nums[mid] < target <= nums[high]: low = mid + 1
            else: high = mid - 1
    return -1

