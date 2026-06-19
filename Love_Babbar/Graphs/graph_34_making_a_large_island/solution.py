# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Step 1: Use DSU to connect all adjacent 1s and calculate the size of each component. Step 2: For each 0, check its 4 neighbors. Find the unique roots of those neighbors. The potential new island size is `1 + sum(size[root])` for each unique root. Find max potential size. Handle case where matrix is all 1s.

def largestIsland(grid: List[List[int]]) -> int:
    n = len(grid)
    parent = list(range(n * n))
    size = [1] * (n * n)
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    def union(i, j):
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            if size[root_i] < size[root_j]:
                parent[root_i] = root_j
                size[root_j] += size[root_i]
            else:
                parent[root_j] = root_i
                size[root_i] += size[root_j]
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        union(r * n + c, nr * n + nc)
    mx = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                components = set()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        components.add(find(nr * n + nc))
                mx = max(mx, 1 + sum(size[comp] for comp in components))
    return mx if mx > 0 else n * n

