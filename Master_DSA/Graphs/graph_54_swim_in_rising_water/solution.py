# Time Complexity: O(N^2 log N)
# Space Complexity: O(N^2)
# Explanation: Use a priority queue to always process the cell with the minimum maximum-elevation so far. `pq` stores `(max_elev_in_path, r, c)`. Push `(grid[0][0], 0, 0)`. While pq is not empty, pop the minimum. If we reach `(n-1, n-1)`, return the `max_elev`. For each neighbor, the new max elevation is `max(max_elev, grid[nr][nc])`. Push to pq if not visited.

import heapq
def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    pq = [(grid[0][0], 0, 0)]
    vis = [[0] * n for _ in range(n)]
    vis[0][0] = 1
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    while pq:
        t, r, c = heapq.heappop(pq)
        if r == n - 1 and c == n - 1: return t
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not vis[nr][nc]:
                vis[nr][nc] = 1
                heapq.heappush(pq, (max(t, grid[nr][nc]), nr, nc))
    return 0

