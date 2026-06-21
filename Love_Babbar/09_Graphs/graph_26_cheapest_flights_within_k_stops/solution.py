# Time Complexity: O(E)
# Space Complexity: O(N + E)
# Explanation: Use a queue storing `(stops, node, cost)`. We don't need a priority queue because stops increase uniformly by 1. Distance array stores min cost to reach each node. Only push to queue if new cost is cheaper. If `stops > k`, skip.

import collections
def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = collections.defaultdict(list)
    for u, v, w in flights:
        adj[u].append((v, w))
    q = collections.deque([(0, src, 0)]) # stops, node, cost
    dist = [float('inf')] * n
    dist[src] = 0
    while q:
        stops, node, cost = q.popleft()
        if stops > k: continue
        for nxt, weight in adj[node]:
            if cost + weight < dist[nxt] and stops <= k:
                dist[nxt] = cost + weight
                q.append((stops + 1, nxt, cost + weight))
    return dist[dst] if dist[dst] != float('inf') else -1

