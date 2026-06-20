# Time Complexity: O(N^3)
# Space Complexity: O(1)
# Explanation: Brute Force: Generate all possible subarrays using three nested loops and find the maximum sum.

def maxSubArray(nums):
    maxi = float('-inf')
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(nums[i:j+1])
            maxi = max(maxi, current_sum)
    return maxi

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Kadane's Algorithm. Keep a running sum. If sum becomes negative, reset it to 0 (a negative prefix will never help a future subarray).

def maxSubArray(nums: list[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return int(max_sum)

