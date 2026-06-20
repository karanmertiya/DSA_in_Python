# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Explanation: MCM Pattern. Add 1 at the beginning and end. Loop lengths from 1 to N. Iterate start `i` and end `j`. Then iterate `k` from `i` to `j`, meaning balloon `k` is the LAST one to burst in the range `[i, j]`. The coins collected are `nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]`.

def maxCoins(nums: List[int]) -> int:
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n, 0, -1):
        for j in range(1, n + 1):
            if i > j: continue
            maxi = float('-inf')
            for k in range(i, j + 1):
                cost = nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j]
                maxi = max(maxi, cost)
            dp[i][j] = maxi
    return dp[1][n]

