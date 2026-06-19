# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Binary Search. If `nums[mid] > nums[mid + 1]`, we are on a descending slope, so a peak must be to the left (or is `mid`). Else, we are on an ascending slope, peak is to the right.

def findPeakElement(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]: high = mid
        else: low = mid + 1
    return low

