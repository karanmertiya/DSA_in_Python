# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: Standard BFS starting from source. Distance of neighbors is `dist[u] + 1`.

import collections
def shortestPath(edges: List[List[int]], n: int, m: int, src: int) -> List[int]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    dist = [1e9] * n
    dist[src] = 0
    q = collections.deque([src])
    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            if dist[node] + 1 < dist[neighbor]:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
    return [d if d != 1e9 else -1 for d in dist]

