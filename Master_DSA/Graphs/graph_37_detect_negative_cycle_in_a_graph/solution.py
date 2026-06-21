# Time Complexity: O(V * E)
# Space Complexity: O(V)
# Explanation: Use Bellman Ford algorithm. Relax all edges V-1 times. Then relax one more time. If any shortest path distance updates in the V-th relaxation, it means there is a negative weight cycle.

def isNegativeWeightCycle(n, edges):
    dist = [1e8] * n
    dist[0] = 0
    for _ in range(n - 1):
        for u, v, wt in edges:
            if dist[u] != 1e8 and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
    for u, v, wt in edges:
        if dist[u] != 1e8 and dist[u] + wt < dist[v]:
            return 1
    return 0

