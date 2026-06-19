# Time Complexity: O(E log E)
# Space Complexity: O(V + E)
# Explanation: Sort all edges by weight. Iterate through sorted edges, if the two vertices do not belong to the same set (using Disjoint Set Union `findParent`), add the edge to MST and `union` the two sets.

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def findUPar(self, node):
        if node == self.parent[node]: return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v: return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

def spanningTree(V: int, adj: List[List[List[int]]]) -> int:
    edges = []
    for i in range(V):
        for neighbor, weight in adj[i]:
            edges.append((weight, i, neighbor))
    edges.sort()
    ds = DisjointSet(V)
    mstWt = 0
    for wt, u, v in edges:
        if ds.findUPar(u) != ds.findUPar(v):
            mstWt += wt
            ds.unionBySize(u, v)
    return mstWt

