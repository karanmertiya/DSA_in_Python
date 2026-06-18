# Time Complexity: O(N<sup>2</sup>) (Trade-off)
# Space Complexity: O(1)
# Explanation: Check all possible subarrays and calculate their sum.

def max_sub_array_brute(nums: list[int]) -> int:
    maxi = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            maxi = max(maxi, curr_sum)
    return maxi

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Kadane's: Maintain `curr_sum`. If `curr_sum` drops below zero, reset it. Track maximum.

def max_sub_array_optimal(nums: list[int]) -> int:
    maxi = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum += num
        maxi = max(maxi, curr_sum)
        if curr_sum < 0: curr_sum = 0
    return maxi

