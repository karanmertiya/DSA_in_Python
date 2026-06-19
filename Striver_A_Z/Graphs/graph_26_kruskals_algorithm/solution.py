# Time Complexity: O(E log E + E * alpha)
# Space Complexity: O(V + E)
# Explanation: Sort all edges by weight. Iterate through sorted edges. Use Disjoint Set Union (DSU) to check if adding the edge forms a cycle. If not, add edge to MST and union the sets.

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def find(self, i):
        if self.parent[i] == i: return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                self.parent[root_i] = root_j
                self.size[root_j] += self.size[root_i]
            else:
                self.parent[root_j] = root_i
                self.size[root_i] += self.size[root_j]

def spanningTree(V, adj):
    edges = []
    for i in range(V):
        for neighbor, wt in adj[i]:
            edges.append((wt, i, neighbor))
    edges.sort()
    ds = DisjointSet(V)
    sum = 0
    for wt, u, v in edges:
        if ds.find(u) != ds.find(v):
            sum += wt
            ds.union(u, v)
    return sum

