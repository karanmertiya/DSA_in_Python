# Time Complexity: O(N * alpha(N))
# Space Complexity: O(N)
# Explanation: Imagine rows and columns are nodes in a bipartite graph. A stone at `(r, c)` connects row `r` and column `c`. The answer is `total_stones - number_of_connected_components`. We can map cols to `col + 10001` to use a single DSU.

def removeStones(stones: List[List[int]]) -> int:
    parent = {}
    components = [0]
    def find(i):
        if i not in parent:
            parent[i] = i
            components[0] += 1
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    def union(i, j):
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            components[0] -= 1
    for r, c in stones:
        union(r, ~c)
    return len(stones) - components[0]

