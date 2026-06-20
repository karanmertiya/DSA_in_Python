# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Explanation: Brute Force: Linear search for each number from 0 to N inside the array.

def missingNumber(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
    return -1

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Using XOR: XORing a number with itself results in 0. XOR all indices `[0,n]` and all elements in `nums`. The missing number will remain.

def missingNumber(nums: list[int]) -> int:
    res = len(nums)
    for i, num in enumerate(nums):
        res ^= i ^ num
    return res

