# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Calculate indegree for all nodes. Push all nodes with indegree 0 to a queue. While queue is not empty, pop a node, add it to result, and decrement indegree of all its adjacent nodes. If indegree becomes 0, push to queue.

def topoSort(V: int, adj: List[List[int]]) -> List[int]:
    indegree = [0] * V
    for i in range(V):
        for node in adj[i]:
            indegree[node] += 1
    q = collections.deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return topo

