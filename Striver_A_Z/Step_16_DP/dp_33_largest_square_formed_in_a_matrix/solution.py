# Time Complexity: O(N * M)
# Space Complexity: O(N * M) or O(M)
# Explanation: `dp[i][j]` is side of max square ending at `(i, j)`. If `mat[i][j] == 1`, `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`. Result is max over all `dp[i][j]`.

def maxSquare(n: int, m: int, mat: List[List[int]]) -> int:
    dp = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(ans, dp[i][j])
    return ans

