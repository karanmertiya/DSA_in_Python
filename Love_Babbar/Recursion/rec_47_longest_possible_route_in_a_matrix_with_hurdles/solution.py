# Time Complexity: O(4^(N*M))
# Space Complexity: O(N*M)
# Explanation: Use a global `max_dist` or pass it by reference. In `solve(r, c, dist)`, if `(r, c) == (dest_r, dest_c)`, `max_dist = max(max_dist, dist)` and return. Mark `(r, c)` as visited. Explore 4 directions. Unmark `(r, c)`.

def longestPath(mat: List[List[int]], xs: int, ys: int, xd: int, yd: int) -> int:
    if mat[xs][ys] == 0 or mat[xd][yd] == 0: return -1
    maxDist = [-1]
    n, m = len(mat), len(mat[0])
    def solve(r, c, dist):
        if r == xd and c == yd:
            maxDist[0] = max(maxDist[0], dist)
            return
        mat[r][c] = 0
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                solve(nr, nc, dist + 1)
        mat[r][c] = 1
    solve(xs, ys, 0)
    return maxDist[0]

