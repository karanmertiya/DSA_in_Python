# Time Complexity: O(2N) (Trade-off)
# Space Complexity: O(1)
# Explanation: Maintain a window counting zeros. If zeros exceed K, shrink from left.

def longest_ones_better(nums: list[int], k: int) -> int:
    left = zeros = max_len = 0
    for right in range(len(nums)):
        if nums[right] == 0: zeros += 1
        while zeros > k:
            if nums[left] == 0: zeros -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Optimal: Never shrink the window, only slide it when invalid. This retains the `max_len` automatically.

def longest_ones_optimal(nums: list[int], k: int) -> int:
    left = zeros = 0
    for right in range(len(nums)):
        if nums[right] == 0: zeros += 1
        if zeros > k:
            if nums[left] == 0: zeros -= 1
            left += 1
    return len(nums) - left

