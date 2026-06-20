# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Step 1: Use DFS to find the first island. Mark all its cells (e.g., set to 2) and push them into a queue for BFS. Step 2: Perform multi-source BFS from the queue. Expand the island level by level. The first time we hit a `1` (which belongs to the second island), the number of layers expanded is the shortest bridge.

import collections
def shortestBridge(grid: List[List[int]]) -> int:
    n = len(grid)
    q = collections.deque()
    def dfs(r, c):
        grid[r][c] = 2
        q.append((r, c))
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                dfs(nr, nc)
    found = False
    for i in range(n):
        if found: break
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                found = True
                break
    steps = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 1: return steps
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        steps += 1
    return steps

