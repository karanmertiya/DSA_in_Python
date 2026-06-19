# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a hash map to store `value -> index`. Iterate through array, check if `target - nums[i]` exists in map. If yes, return current index and mapped index. Else, store current value and index.

def twoSum(nums, target):
    m = {}
    for i, num in enumerate(nums):
        if target - num in m:
            return [m[target - num], i]
        m[num] = i
    return []

