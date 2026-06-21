# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Push all land cells (1s) into a queue and mark them as visited. Perform BFS outward. The last water cell processed gives the maximum distance. Track layers/steps during BFS.

import collections
def maxDistance(grid: List[List[int]]) -> int:
    n = len(grid)
    q = collections.deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1: q.append((i, j))
    if not q or len(q) == n * n: return -1
    dist = -1
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc))
        dist += 1
    return dist

