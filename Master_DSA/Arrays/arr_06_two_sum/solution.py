# Time Complexity: O(N<sup>2</sup>) (Trade-off)
# Space Complexity: O(1)
# Explanation: Nested loops to check all possible pairs.

def two_sum_brute(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Use a Hash Map to store elements and their indices. Check for `target - current`.

def two_sum_optimal(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in hash_map:
            return [hash_map[needed], i]
        hash_map[num] = i
    return []

