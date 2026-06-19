# Time Complexity: O(E log V)
# Space Complexity: O(V)
# Explanation: Use a Min-Heap. `dist` array initialized to infinity. Push `{0, src}` to PQ. Pop `node`. If `dist[node] + weight < dist[adjNode]`, update `dist[adjNode]` and push `{dist[adjNode], adjNode}` to PQ.

import heapq
def dijkstra(V: int, adj: List[List[List[int]]], S: int) -> List[int]:
    pq = [(0, S)]
    dist = [1e9] * V
    dist[S] = 0
    while pq:
        dis, node = heapq.heappop(pq)
        for adjNode, edgeWeight in adj[node]:
            if dis + edgeWeight < dist[adjNode]:
                dist[adjNode] = dis + edgeWeight
                heapq.heappush(pq, (dist[adjNode], adjNode))
    return dist

