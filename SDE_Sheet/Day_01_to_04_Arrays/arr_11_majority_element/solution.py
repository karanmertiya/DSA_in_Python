# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Explanation: Brute Force: Use two nested loops to count occurrences of each element.

def majorityElement(nums):
    n = len(nums)
    for num in nums:
        if nums.count(num) > n // 2:
            return num
    return -1

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Optimal: Moore's Voting Algorithm. Track a candidate and a counter. Increment if same as candidate, decrement if different. If zero, pick new candidate.

def majorityElement(nums: list[int]) -> int:
    count = candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

