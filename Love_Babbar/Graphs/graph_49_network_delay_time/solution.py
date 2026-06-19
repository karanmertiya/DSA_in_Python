# Time Complexity: O(E log V)
# Space Complexity: O(N + E)
# Explanation: Find shortest path from source node `k` to all other nodes using Dijkstra's algorithm. The answer is the maximum distance among all nodes. If any node is unreachable (distance is infinity), return -1.

import collections, heapq
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adj = collections.defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    pq = [(0, k)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]: continue
        for nxt, wt in adj[node]:
            if d + wt < dist[nxt]:
                dist[nxt] = d + wt
                heapq.heappush(pq, (dist[nxt], nxt))
    ans = max(dist[1:])
    return ans if ans != float('inf') else -1

