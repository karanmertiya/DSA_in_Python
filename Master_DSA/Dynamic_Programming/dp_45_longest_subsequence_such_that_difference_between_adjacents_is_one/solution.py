# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Use a 1D DP array `dp` where `dp[i]` is the length of the longest subsequence ending at `i`. For each `i`, check all `j < i`. If `abs(A[i] - A[j]) == 1`, update `dp[i] = max(dp[i], dp[j] + 1)`.

def longestSubsequence(N, A):
    dp = [1] * N
    ans = 1
    for i in range(1, N):
        for j in range(i):
            if abs(A[i] - A[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])
    return ans

