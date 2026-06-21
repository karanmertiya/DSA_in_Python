# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Perform BFS or DFS starting from all 4 corners simultaneously or individually. At each cell `(r, c)`, the jump size is `val = grid[r][c]`. We can move to `(r+val, c)`, `(r-val, c)`, `(r, c+val)`, `(r, c-val)`. Target is `(N/2, N/2)`.

import collections
def solve(grid: List[List[int]]):
    n = len(grid)
    q = collections.deque([(0,0), (0,n-1), (n-1,0), (n-1,n-1)])
    vis = set(q)
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        r, c = q.popleft()
        if r == n // 2 and c == n // 2: return True
        val = grid[r][c]
        if val == 0: continue
        for i in range(4):
            nr, nc = r + dr[i] * val, c + dc[i] * val
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in vis:
                vis.add((nr, nc))
                q.append((nr, nc))
    return False

