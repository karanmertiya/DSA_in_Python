# Time Complexity: O(4^(M*N))
# Space Complexity: O(M*N)
# Explanation: Use Backtracking. Start from the source, mark it as visited, recursively find the longest path from all valid unvisited adjacent cells, add 1 to the maximum among them. Unmark the cell after returning.

def findLongestPath(mat, i, j, di, dj, curr, max_dist, vis):
    if i == di and j == dj:
        max_dist[0] = max(max_dist[0], curr)
        return
    vis[i][j] = True
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    for k in range(4):
        nr, nc = i + dr[k], j + dc[k]
        if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]) and mat[nr][nc] == 1 and not vis[nr][nc]:
            findLongestPath(mat, nr, nc, di, dj, curr + 1, max_dist, vis)
    vis[i][j] = False

