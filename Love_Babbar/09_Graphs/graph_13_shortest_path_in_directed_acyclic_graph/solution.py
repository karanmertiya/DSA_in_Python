# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: Perform Topological Sort. Then iterate through the topologically sorted vertices. For each vertex `u`, relax its neighbors: `dist[v] = min(dist[v], dist[u] + weight)`. Return `dist` array.

def shortestPath(N: int, M: int, edges: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(N)]
    for u, v, wt in edges:
        adj[u].append((v, wt))
    vis = [0] * N
    st = []
    def topoSort(node):
        vis[node] = 1
        for v, wt in adj[node]:
            if not vis[v]: topoSort(v)
        st.append(node)
    for i in range(N):
        if not vis[i]: topoSort(i)
    dist = [1e9] * N
    dist[0] = 0
    while st:
        node = st.pop()
        if dist[node] != 1e9:
            for v, wt in adj[node]:
                if dist[node] + wt < dist[v]:
                    dist[v] = dist[node] + wt
    return [d if d != 1e9 else -1 for d in dist]

