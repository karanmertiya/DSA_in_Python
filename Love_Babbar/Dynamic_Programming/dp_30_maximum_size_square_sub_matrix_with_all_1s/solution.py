# Time Complexity: O(N * M)
# Space Complexity: O(M)
# Explanation: Use DP. `dp[i][j]` stores the size of the maximum square ending at cell `(i, j)`. If `mat[i][j] == 1`, `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`.

def maxSquare(n, m, mat):
    prev = [0] * m
    curr = [0] * m
    ans = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                if i == 0 or j == 0: curr[j] = 1
                else: curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1
                ans = max(ans, curr[j])
            else: curr[j] = 0
        prev = list(curr)
    return ans

