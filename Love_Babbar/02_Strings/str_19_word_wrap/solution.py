# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Use Dynamic Programming. `dp[i]` represents the minimum cost to wrap words from index `i` to the end. Iterate backward and try placing different numbers of words on the current line.

def solveWordWrap(nums, k):
    n = len(nums)
    dp = [0] * n
    dp[n - 1] = 0
    for i in range(n - 2, -1, -1):
        currlen = -1
        dp[i] = float('inf')
        for j in range(i, n):
            currlen += (nums[j] + 1)
            if currlen > k: break
            if j == n - 1:
                dp[i] = 0
            else:
                cost = (k - currlen) ** 2 + dp[j + 1]
                dp[i] = min(dp[i], cost)
    return dp[0]

