# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Floyd's Tortoise and Hare (Cycle Detection). Treat the array values as pointers to the next index. Since there's a duplicate, a cycle must exist. Find the intersection point of slow and fast pointers, then find the entrance to the cycle.

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

