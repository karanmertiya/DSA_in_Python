# Time Complexity: O(rows * cols)
# Space Complexity: O(rows * cols)
# Explanation: Use a Queue for BFS. Find all initially rotten oranges and push them into the queue with time 0. Count total fresh oranges. Pop an orange, rot its adjacent fresh oranges, push them to the queue with `time + 1`, and decrement fresh count. Return the max time if fresh count is 0, else -1.

from collections import deque
def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh_cnt = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2: q.append((i, j, 0))
            elif grid[i][j] == 1: fresh_cnt += 1
    tm, cnt = 0, 0
    while q:
        r, c, t = q.popleft()
        tm = max(tm, t)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                q.append((nr, nc, t + 1))
                cnt += 1
    return tm if cnt == fresh_cnt else -1

