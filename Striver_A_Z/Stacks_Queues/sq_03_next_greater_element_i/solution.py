# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N)
# Explanation: Iterate backwards maintaining a strictly decreasing Monotonic Stack. The top of the stack is the next greater element.

def next_greater_element(nums: list[int]) -> list[int]:
    res = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
    return res

