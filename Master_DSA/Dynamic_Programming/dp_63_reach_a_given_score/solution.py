# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: `dp[i]` represents number of ways to reach score `i`. Init `dp[0] = 1`. For each score option (3, 5, 10), iterate from option to `n`, `dp[i] += dp[i - option]`.

def count(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    scores = [3, 5, 10]
    for s in scores:
        for i in range(s, n + 1):
            dp[i] += dp[i - s]
    return dp[n]

