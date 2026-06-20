# Time Complexity: O(E log V)
# Space Complexity: O(E + V)
# Explanation: Prim's Algorithm. Use a Min-Heap `(weight, node)`. Always pick the smallest available edge connecting the MST to an unvisited node.

import heapq
def spanningTree(V: int, adj: List[List[List[int]]]) -> int:
    pq = [(0, 0)]
    vis = [0] * V
    sum_val = 0
    while pq:
        wt, node = heapq.heappop(pq)
        if vis[node] == 1: continue
        vis[node] = 1
        sum_val += wt
        for adjNode, edW in adj[node]:
            if not vis[adjNode]: heapq.heappush(pq, (edW, adjNode))
    return sum_val

