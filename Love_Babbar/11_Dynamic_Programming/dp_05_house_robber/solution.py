# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Space Optimized DP. Maintain two variables: `prev1` (max up to previous house) and `prev2` (max up to the house before previous). `curr = max(num + prev2, prev1)`.

def rob(nums: list[int]) -> int:
    prev1, prev2 = 0, 0
    for num in nums:
        curr = max(num + prev2, prev1)
        prev2 = prev1
        prev1 = curr
    return prev1

