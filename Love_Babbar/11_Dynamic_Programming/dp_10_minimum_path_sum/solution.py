# Time Complexity: O(N * M)
# Space Complexity: O(M)
# Explanation: DP on Grids. Space optimize to 1D. `cur[j] = grid[i][j] + min(up, left)`.

def minPathSum(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    prev = [0] * m
    for i in range(n):
        cur = [0] * m
        for j in range(m):
            if i == 0 and j == 0: cur[j] = grid[i][j]
            else:
                up, left = grid[i][j], grid[i][j]
                up += prev[j] if i > 0 else float('inf')
                left += cur[j-1] if j > 0 else float('inf')
                cur[j] = min(up, left)
        prev = cur
    return prev[-1]

