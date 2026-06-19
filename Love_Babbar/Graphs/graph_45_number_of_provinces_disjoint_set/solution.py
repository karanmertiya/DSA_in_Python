# Time Complexity: O(V^2 * alpha)
# Space Complexity: O(V)
# Explanation: Initialize Disjoint Set for `n` nodes. Iterate through `isConnected` matrix. If `isConnected[i][j] == 1`, union `i` and `j`. After processing all edges, count how many nodes are their own parents (`parent[i] == i`).

# Use DisjointSet class
def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    ds = DisjointSet(n)
    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1: ds.union(i, j)
    return sum(1 for i in range(n) if ds.find(i) == i)

