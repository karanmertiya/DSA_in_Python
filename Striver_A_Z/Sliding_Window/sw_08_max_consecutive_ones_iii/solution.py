# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a sliding window. Expand the right pointer. If the element is 0, increment a zero counter. While the zero counter > k, shrink the window from the left by moving the left pointer and decrementing the zero counter if left element is 0. The max window size is the answer.

def longestOnes(nums, k):
    left = 0
    zeroes = 0
    max_len = 0
    for right in range(len(nums)):
        if nums[right] == 0: zeroes += 1
        while zeroes > k:
            if nums[left] == 0: zeroes -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

