# Time Complexity: O(E log V)
# Space Complexity: O(V)
# Explanation: Min-heap (priority queue) to repeatedly extract the node with the minimum distance and relax its neighbors.

def dijkstra(V: int, adj: List[List[List[int]]], S: int) -> List[int]:
    import heapq
    dist = [float('inf')] * V
    dist[S] = 0
    pq = [(0, S)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]: continue
        for nxt, weight in adj[node]:
            if d + weight < dist[nxt]:
                dist[nxt] = d + weight
                heapq.heappush(pq, (dist[nxt], nxt))
    return dist

