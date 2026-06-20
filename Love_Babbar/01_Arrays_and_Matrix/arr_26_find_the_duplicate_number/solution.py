# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Floyd's Tortoise and Hare (Cycle Detection). Fast and slow pointer. Guaranteed cycle because of Pigeonhole Principle (numbers map to index ranges).

def findDuplicate(nums: List[int]) -> int:
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

