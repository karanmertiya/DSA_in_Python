# Time Complexity: O(E * alpha(N))
# Space Complexity: O(N)
# Explanation: If total edges < n - 1, impossible. Use DSU to count number of connected components `C` and number of extra edges `E`. An edge is extra if `find(u) == find(v)`. We need `C - 1` edges to connect `C` components. Since total edges >= n - 1, we guaranteed have enough extra edges. Answer is `C - 1`.

def makeConnected(n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1: return -1
    parent = list(range(n))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    components = n
    for u, v in connections:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            components -= 1
    return components - 1

