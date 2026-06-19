# Time Complexity: O(E log V)
# Space Complexity: O(V)
# Explanation: Prim's Algorithm. Push `{0, 0}` to Min-Heap. If node is visited, continue. Mark visited, add weight to sum. Push all adjacent unvisited nodes to Heap.

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

