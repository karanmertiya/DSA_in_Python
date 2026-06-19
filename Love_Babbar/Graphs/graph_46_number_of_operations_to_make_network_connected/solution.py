# Time Complexity: O(E * alpha)
# Space Complexity: O(V)
# Explanation: If total edges < n - 1, return -1. Count extra edges while building DSU. If union fails (already connected), it's an extra edge. Number of operations to connect components is `components - 1`. If `extraEdges >= components - 1`, return `components - 1`.

def makeConnected(n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1: return -1
    ds = DisjointSet(n)
    extraEdges = 0
    for u, v in connections:
        if not ds.union(u, v): extraEdges += 1
    components = sum(1 for i in range(n) if ds.find(i) == i)
    if extraEdges >= components - 1: return components - 1
    return -1

