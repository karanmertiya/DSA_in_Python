# Time Complexity: O(N * M)
# Space Complexity: O(N * M) auxiliary
# Explanation: Traverse grid. Whenever a '1' is found, increment counter and trigger BFS/DFS to sink the island (mark '0').

def numIslands(grid: List[List[str]]) -> int:
    if not grid: return 0
    def dfs(r, c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] == '0': return
        grid[r][c] = '0'
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count

