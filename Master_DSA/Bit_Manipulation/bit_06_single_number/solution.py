# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Use a Hash Map to count occurrences. Return the element with count 1.

def single_number(nums: list[int]) -> int:
    ans = 0
    for num in nums:
        ans ^= num
    return ans

