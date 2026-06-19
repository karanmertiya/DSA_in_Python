# Time Complexity: O(M * N)
# Space Complexity: O(M * N)
# Explanation: Iterate through each cell. When a '1' is found, increment the island count and start a DFS/BFS to mark all connected '1's as '0' (visited).

def numIslands(grid):
    if not grid: return 0
    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0': return
        grid[r][c] = '0'
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count

