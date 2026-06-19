# Time Complexity: O(E log V)
# Space Complexity: O(V + E)
# Explanation: Use a Min Heap to store `(weight, node)`. Start from node 0. Pop min edge. If node is unvisited, add weight to sum, mark visited, and push its unvisited neighbors to the heap.

import heapq
def spanningTree(V, adj):
    pq = [(0, 0)]
    vis = [False] * V
    sum_wt = 0
    while pq:
        wt, node = heapq.heappop(pq)
        if vis[node]: continue
        vis[node] = True
        sum_wt += wt
        for nbr, edW in adj[node]:
            if not vis[nbr]:
                heapq.heappush(pq, (edW, nbr))
    return sum_wt

