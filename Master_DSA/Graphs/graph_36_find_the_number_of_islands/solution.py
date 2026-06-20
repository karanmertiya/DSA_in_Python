# Time Complexity: O(N * M)
# Space Complexity: O(N * M) worst case stack
# Explanation: Traverse the grid. When a '1' is found, increment island count and use DFS/BFS to mark all its 8-connected neighbors as '0' (or visited) to avoid recounting.

def numIslands(grid: List[List[str]]) -> int:
    if not grid: return 0
    n, m = len(grid), len(grid[0])
    def dfs(r, c):
        grid[r][c] = '0'
        for delrow in [-1, 0, 1]:
            for delcol in [-1, 0, 1]:
                nrow, ncol = r + delrow, c + delcol
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1':
                    dfs(nrow, ncol)
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count

