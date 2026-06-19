# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Step 1: Traverse the grid. For each `1`, union it with its `1` neighbors. Calculate the size of each component using DSU. Step 2: Traverse again. For each `0`, check its 4 neighbors. Find unique ultimate parents among neighbors, sum their sizes, and add 1 (for the flipped `0`). Keep track of the maximum size found.

# Uses DSU with rank/size
def largestIsland(grid: List[List[int]]) -> int:
    n = len(grid)
    ds = DisjointSet(n * n)
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0: continue
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    ds.union(r * n + c, nr * n + nc)
    mx = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1: continue
            components = set()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    components.add(ds.find(nr * n + nc))
            sizeTotal = sum(ds.size[root] for root in components)
            mx = max(mx, sizeTotal + 1)
    for cell in range(n * n):
        mx = max(mx, ds.size[ds.find(cell)])
    return mx

