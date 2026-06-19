# Time Complexity: O(E log V)
# Space Complexity: O(E + V)
# Explanation: Start from node 0. Push `(0, 0)` -> `(weight, node)` into PQ. Maintain `visited` array. Pop min edge. If not visited, mark visited, add weight to sum. Traverse its neighbors; if not visited, push to PQ.

import heapq
def spanningTree(V, adj):
    pq = [(0, 0)]
    vis = [0] * V
    sum_wt = 0
    while pq:
        wt, node = heapq.heappop(pq)
        if vis[node]: continue
        vis[node] = 1
        sum_wt += wt
        for neighbor in adj[node]:
            adjNode, edW = neighbor[0], neighbor[1]
            if not vis[adjNode]:
                heapq.heappush(pq, (edW, adjNode))
    return sum_wt

