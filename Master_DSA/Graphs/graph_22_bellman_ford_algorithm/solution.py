# Time Complexity: O(V * E)
# Space Complexity: O(V)
# Explanation: Relax all E edges V-1 times. If any edge can still be relaxed in the Vth iteration, then there's a negative cycle.

def bellman_ford(V: int, edges: List[List[int]], S: int) -> List[int]:
    dist = [int(1e8)] * V
    dist[S] = 0
    for _ in range(V - 1):
        for u, v, wt in edges:
            if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
    for u, v, wt in edges:
        if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
            return [-1]
    return dist

