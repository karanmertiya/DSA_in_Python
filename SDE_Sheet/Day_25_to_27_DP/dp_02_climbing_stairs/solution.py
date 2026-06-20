# Time Complexity: O(N)
# Space Complexity: O(1) (Constraint)
# Explanation: Space Optimization (Bottom-Up): Since state `n` only depends on `n-1` and `n-2`, we only need two variables.

def climbStairs(n: int) -> int:
    if n <= 1: return 1
    prev2, prev = 1, 1
    for i in range(2, n + 1):
        curr = prev + prev2
        prev2, prev = prev, curr
    return prev

