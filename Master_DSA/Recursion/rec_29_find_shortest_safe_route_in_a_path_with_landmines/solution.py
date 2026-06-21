# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
# Explanation: First, mark all adjacent cells of landmines as unsafe. Then start from each cell in the first column and use BFS or Backtracking to find the shortest path to the last column, avoiding unsafe cells.

from collections import deque
def findShortestPath(mat):
    R, C = len(mat), len(mat[0])
    grid = [[1] * C for _ in range(R)]
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(R):
        for j in range(C):
            if mat[i][j] == 0:
                grid[i][j] = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < R and 0 <= nc < C: grid[nr][nc] = 0
    q = deque()
    vis = [[False] * C for _ in range(R)]
    for i in range(R):
        if grid[i][0] == 1:
            q.append((i, 0, 1))
            vis[i][0] = True
    while q:
        r, c, dist = q.popleft()
        if c == C - 1: return dist
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and not vis[nr][nc]:
                vis[nr][nc] = True
                q.append((nr, nc, dist + 1))
    return -1

