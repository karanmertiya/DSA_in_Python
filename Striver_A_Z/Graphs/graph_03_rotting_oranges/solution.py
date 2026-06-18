# Time Complexity: O(M * N)
# Space Complexity: O(M * N)
# Explanation: Multi-source BFS. Put all initially rotten oranges in queue. Process level by level.

from collections import deque
def orangesRotting(grid: list[list[int]]) -> int:
    q = deque()
    fresh = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2: q.append((i, j))
            elif grid[i][j] == 1: fresh += 1
    time = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
        time += 1
    return time if fresh == 0 else -1

