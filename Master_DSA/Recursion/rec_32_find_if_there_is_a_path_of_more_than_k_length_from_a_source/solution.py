# Time Complexity: O(V!)
# Space Complexity: O(V)
# Explanation: Use Backtracking to perform DFS traversal from the source. Mark the current vertex as visited, subtract the edge weight from `k`, and recursively call for all adjacent unvisited vertices. If `k <= 0`, return true. Backtrack by unmarking the vertex.

def pathMoreThanK(src, k, adj, vis):
    if k <= 0: return True
    vis[src] = True
    for v, w in adj[src]:
        if not vis[v]:
            if pathMoreThanK(v, k - w, adj, vis):
                return True
    vis[src] = False
    return False

