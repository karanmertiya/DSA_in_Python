# Time Complexity: O(E log E)
# Space Complexity: O(E + V)
# Explanation: Extract all edges as `(weight, u, v)`. Sort edges by weight. Iterate through sorted edges. Use Disjoint Set (Union-Find) to check if `u` and `v` are in the same component. If not, union them and add weight to sum.

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def spanningTree(V, adj):
    edges = []
    for i in range(V):
        for neighbor in adj[i]:
            edges.append((neighbor[1], i, neighbor[0]))
    edges.sort()
    ds = DisjointSet(V)
    mst_wt = 0
    for wt, u, v in edges:
        if ds.union(u, v):
            mst_wt += wt
    return mst_wt

