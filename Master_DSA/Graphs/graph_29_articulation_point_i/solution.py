# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Maintain `tin` (insertion time) and `low` (lowest insertion time reachable). A node `u` is an articulation point if `low[v] >= tin[u]` (and it's not root). If root, it's an articulation point if it has >1 children in DFS tree.

class Solution:
    def __init__(self):
        self.timer = 0
    def dfs(self, node, parent, vis, tin, low, mark, adj):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0
        for it in adj[node]:
            if it == parent: continue
            if not vis[it]:
                self.dfs(it, node, vis, tin, low, mark, adj)
                low[node] = min(low[node], low[it])
                if low[it] >= tin[node] and parent != -1:
                    mark[node] = 1
                child += 1
            else:
                low[node] = min(low[node], tin[it])
        if child > 1 and parent == -1:
            mark[node] = 1
    def articulationPoints(self, V, adj):
        vis = [0] * V
        tin = [0] * V
        low = [0] * V
        mark = [0] * V
        for i in range(V):
            if not vis[i]:
                self.dfs(i, -1, vis, tin, low, mark, adj)
        ans = []
        for i in range(V):
            if mark[i] == 1: ans.append(i)
        if len(ans) == 0: return [-1]
        return ans

