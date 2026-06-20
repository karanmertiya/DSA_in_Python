# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Start from bottom row up. `dp[i][j] = matrix[i][j] + max(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1])`. The answer is max value in `dp[0]`.

def maximumPath(N: int, Matrix: List[List[int]]) -> int:
    prev = Matrix[-1][:]
    for i in range(N - 2, -1, -1):
        curr = [0] * N
        for j in range(N):
            up = Matrix[i][j] + prev[j]
            ld = Matrix[i][j] + prev[j-1] if j > 0 else 0
            rd = Matrix[i][j] + prev[j+1] if j < N - 1 else 0
            curr[j] = max(up, ld, rd)
        prev = curr
    return max(prev)

