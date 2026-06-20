# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def twoSum(nums: list[int], target: int) -> list[int]:
    mpp = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in mpp:
            return [mpp[needed], i]
        mpp[num] = i
    return []

# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Optimal: Iterate while storing numbers and their indices in a hash map. Check if `target - num` already exists.

def twoSum(nums: list[int], target: int) -> list[int]:
    mpp = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in mpp:
            return [mpp[needed], i]
        mpp[num] = i
    return []

