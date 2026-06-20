# Time Complexity: O(N^2 * alpha(N))
# Space Complexity: O(N)
# Explanation: Create DSU of size `n`. For every edge in `isConnected`, union the two nodes. The number of provinces is the number of nodes where `find(i) == i`.

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
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
def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    ds = DisjointSet(n)
    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1:
                ds.unionBySize(i, j)
    cnt = 0
    for i in range(n):
        if ds.findUPar(i) == i:
            cnt += 1
    return cnt

