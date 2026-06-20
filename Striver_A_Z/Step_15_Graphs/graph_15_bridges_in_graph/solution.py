# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: Tarjan's algorithm. Maintain `tin` (time of insertion) and `low` (lowest time reachable). If `low[neighbor] > tin[node]`, the edge `(node, neighbor)` is a bridge. Update `low[node] = min(low[node], low[neighbor])`.

def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    adj = [[] for _ in range(n)]
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)
    vis = [0] * n
    tin, low = [0] * n, [0] * n
    bridges = []
    timer = 1
    def dfs(node, parent):
        nonlocal timer
        vis[node] = 1
        tin[node] = low[node] = timer
        timer += 1
        for neighbor in adj[node]:
            if neighbor == parent: continue
            if not vis[neighbor]:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > tin[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], low[neighbor])
    dfs(0, -1)
    return bridges

