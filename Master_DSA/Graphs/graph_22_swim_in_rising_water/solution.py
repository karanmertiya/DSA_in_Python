# Time Complexity: O(N^2 log N)
# Space Complexity: O(N^2)
# Explanation: Use a priority queue (Dijkstra variant). The cost to reach a cell is `max(cost_of_previous_cell, grid[r][c])`. Extract min cost cell, relax neighbors.

import heapq
def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    pq = [(grid[0][0], 0, 0)]
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = grid[0][0]
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    while pq:
        d, r, c = heapq.heappop(pq)
        if r == n - 1 and c == n - 1: return d
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                next_d = max(d, grid[nr][nc])
                if next_d < dist[nr][nc]:
                    dist[nr][nc] = next_d
                    heapq.heappush(pq, (next_d, nr, nc))
    return 0

