# Time Complexity: O(E log V)
# Space Complexity: O(V + E)
# Explanation: Modify Dijkstra's. Keep `dist` array and `ways` array. When relaxing an edge: if `curr_dist + weight < dist[neighbor]`, update `dist`, push to PQ, and `ways[neighbor] = ways[curr_node]`. If `curr_dist + weight == dist[neighbor]`, `ways[neighbor] = (ways[neighbor] + ways[curr_node]) % MOD`.

import collections, heapq
def countPaths(n: int, roads: List[List[int]]) -> int:
    adj = collections.defaultdict(list)
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))
    heap = [(0, 0)]
    dist = [float('inf')] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1
    mod = 10**9 + 7
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]: continue
        for nxt, weight in adj[node]:
            if d + weight < dist[nxt]:
                dist[nxt] = d + weight
                ways[nxt] = ways[node]
                heapq.heappush(heap, (dist[nxt], nxt))
            elif d + weight == dist[nxt]:
                ways[nxt] = (ways[nxt] + ways[node]) % mod
    return ways[n-1]

