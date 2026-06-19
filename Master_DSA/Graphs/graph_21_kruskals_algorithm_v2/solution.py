# Time Complexity: O(E log E)
# Space Complexity: O(V + E)
# Explanation: Sort all edges by weight. Use a Disjoint Set (Union-Find) to maintain components. Iterate through sorted edges, and if adding the edge doesn't form a cycle (i.e. nodes belong to different sets), add its weight to MST and union the sets.

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def find(self, node):
        if node == self.parent[node]: return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
def spanningTree(V, adj):
    edges = []
    for i in range(V):
        for nbr, wt in adj[i]: edges.append((wt, i, nbr))
    edges.sort()
    ds = DisjointSet(V)
    mst_wt = 0
    for wt, u, v in edges:
        if ds.find(u) != ds.find(v):
            mst_wt += wt
            ds.union(u, v)
    return mst_wt

