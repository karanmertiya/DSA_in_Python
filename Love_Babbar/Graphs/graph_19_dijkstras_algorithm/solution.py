# Time Complexity: O(E log V)
# Space Complexity: O(V)
# Explanation: Initialize distances to infinity, and source distance to 0. Use a Min Heap (priority queue) to store `{dist, vertex}`. Pop the vertex with min distance, and relax its neighbors. If a shorter path is found to a neighbor, push it to the queue.

import heapq
def dijkstra(V, adj, S):
    dist = [int(1e9)] * V
    dist[S] = 0
    pq = [(0, S)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]: continue
        for v, wt in adj[node]:
            if d + wt < dist[v]:
                dist[v] = d + wt
                heapq.heappush(pq, (dist[v], v))
    return dist

