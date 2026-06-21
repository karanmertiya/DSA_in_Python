# Time Complexity: O(N * M * M * 9)
# Space Complexity: O(M * M)
# Explanation: Robots move simultaneously. State is `dp[row][col1][col2]`. Try all 9 combinations of moves for both robots.

def cherryPickup(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    front = [[0]*m for _ in range(m)]
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2: front[j1][j2] = grid[n-1][j1]
            else: front[j1][j2] = grid[n-1][j1] + grid[n-1][j2]
    for i in range(n-2, -1, -1):
        cur = [[0]*m for _ in range(m)]
        for j1 in range(m):
            for j2 in range(m):
                maxi = -int(1e9)
                for dj1 in [-1, 0, 1]:
                    for dj2 in [-1, 0, 1]:
                        val = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
                        if 0 <= j1+dj1 < m and 0 <= j2+dj2 < m:
                            val += front[j1+dj1][j2+dj2]
                        else: val += -int(1e9)
                        maxi = max(maxi, val)
                cur[j1][j2] = maxi
        front = cur
    return front[0][m-1]

