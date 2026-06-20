# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Remove the given edge `(c, d)` from the graph. Then run a DFS/BFS from `c`. If `d` is not reachable from `c`, then `(c, d)` was a bridge.

def isBridge(V, adj, c, d):
    vis = [False] * V
    def dfs(node):
        vis[node] = True
        for nbr in adj[node]:
            if (node == c and nbr == d) or (node == d and nbr == c): continue
            if not vis[nbr]: dfs(nbr)
    dfs(c)
    return 1 if not vis[d] else 0

