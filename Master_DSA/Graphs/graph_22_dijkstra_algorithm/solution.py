# Time Complexity: O(E log V)
# Space Complexity: O(V + E)
# Explanation: Use a min-heap to always pick the node with the minimum distance. Relax its adjacent edges. If `dist[node] + weight < dist[adjNode]`, update distance and push to priority queue.

import heapq
def dijkstra(V: int, adj: List[List[List[int]]], S: int) -> List[int]:
    pq = [(0, S)]
    dist = [float('inf')] * V
    dist[S] = 0
    while pq:
        dis, node = heapq.heappop(pq)
        if dis > dist[node]: continue
        for adjNode, edgeWeight in adj[node]:
            if dis + edgeWeight < dist[adjNode]:
                dist[adjNode] = dis + edgeWeight
                heapq.heappush(pq, (dist[adjNode], adjNode))
    return dist

