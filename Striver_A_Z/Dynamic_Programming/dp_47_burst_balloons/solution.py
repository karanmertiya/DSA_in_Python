# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Explanation: Add 1 to both ends of `nums`. `dp[i][j]` is max coins from bursting balloons strictly between `i` and `j`. Guess which balloon `k` (between `i` and `j`) is the LAST one to burst. Coins gained = `nums[i] * nums[k] * nums[j]`. Total = `dp[i][k] + dp[k][j] + coins`.

def maxCoins(nums: List[int]) -> int:
    a = [1] + nums + [1]
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
    return dp[0][n-1]

