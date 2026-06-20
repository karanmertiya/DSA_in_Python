# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Kahn's Algorithm (BFS) using in-degrees. Add nodes with 0 in-degree to a queue. Pop, append to result, and decrement in-degrees of neighbors.

def topoSort(V: int, adj: List[List[int]]) -> List[int]:
    from collections import deque
    indegree = [0] * V
    for i in range(V):
        for nxt in adj[i]: indegree[nxt] += 1
    q = deque([i for i in range(V) if indegree[i] == 0])
    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        for nxt in adj[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0: q.append(nxt)
    return topo

