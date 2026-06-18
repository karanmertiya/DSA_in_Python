# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) + O(N) Recursion Stack
# Explanation: Memoization (Top-Down): Recursive tree caching already solved subproblems in an array.

def climb_stairs_memo(n: int) -> int:
    dp = [-1] * (n + 1)
    def solve(n):
        if n <= 1: return 1
        if dp[n] != -1: return dp[n]
        dp[n] = solve(n - 1) + solve(n - 2)
        return dp[n]
    return solve(n)

# Time Complexity: O(N)
# Space Complexity: O(1) (Constraint)
# Explanation: Space Optimization (Bottom-Up): Since state `n` only depends on `n-1` and `n-2`, we only need two variables.

def climb_stairs_optimal(n: int) -> int:
    if n <= 1: return 1
    prev2 = 1
    prev = 1
    for i in range(2, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev

