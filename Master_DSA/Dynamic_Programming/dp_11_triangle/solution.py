# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Start from bottom row and move upwards. `dp[j] = triangle[i][j] + min(dp[j], dp[j+1])`.

def minimumTotal(triangle: List[List[int]]) -> int:
    n = len(triangle)
    front = triangle[-1][:]
    for i in range(n-2, -1, -1):
        cur = [0] * n
        for j in range(i, -1, -1):
            cur[j] = triangle[i][j] + min(front[j], front[j+1])
        front = cur
    return front[0]

