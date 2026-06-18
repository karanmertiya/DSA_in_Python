# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Using XOR: XORing a number with itself results in 0. XOR all indices `[0,n]` and all elements in `nums`. The missing number will remain.

def missingNumber(nums: list[int]) -> int:
    res = len(nums)
    for i, num in enumerate(nums):
        res ^= i ^ num
    return res

