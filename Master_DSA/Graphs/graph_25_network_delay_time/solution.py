# Time Complexity: O(E log V)
# Space Complexity: O(V + E)
# Explanation: Standard Dijkstra's shortest path from node `k`. Return the maximum value in the distances array. If any node remains unvisited (dist == inf), return -1.

import heapq
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adj = collections.defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    pq = [(0, k)]
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    while pq:
        time, node = heapq.heappop(pq)
        if time > dist[node]: continue
        for adjNode, wt in adj[node]:
            if time + wt < dist[adjNode]:
                dist[adjNode] = time + wt
                heapq.heappush(pq, (time + wt, adjNode))
    mx = max(dist.values())
    return mx if mx != float('inf') else -1

