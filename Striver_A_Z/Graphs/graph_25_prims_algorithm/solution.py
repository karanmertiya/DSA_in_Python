# Time Complexity: O(E log V)
# Space Complexity: O(V)
# Explanation: Same as previous. Min Heap of `{weight, node}`.

import heapq
def spanningTree(V: int, adj: List[List[List[int]]]) -> int:
    pq = [(0, 0)]
    vis = [0] * V
    sum = 0
    while pq:
        wt, node = heapq.heappop(pq)
        if vis[node]: continue
        vis[node] = 1
        sum += wt
        for adjNode, edW in adj[node]:
            if not vis[adjNode]:
                heapq.heappush(pq, (edW, adjNode))
    return sum

