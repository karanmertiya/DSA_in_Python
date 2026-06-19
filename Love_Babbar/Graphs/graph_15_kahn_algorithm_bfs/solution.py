# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Compute in-degrees for all nodes. Push nodes with 0 in-degree to a queue. Pop, add to answer, and reduce in-degrees of neighbors. If a neighbor reaches 0, push it.

def topoSort(V: int, adj: List[List[int]]) -> List[int]:
    indegree = [0] * V
    for i in range(V):
        for it in adj[i]: indegree[it] += 1
    q = [i for i in range(V) if indegree[i] == 0]
    topo = []
    while q:
        node = q.pop(0)
        topo.append(node)
        for it in adj[node]:
            indegree[it] -= 1
            if indegree[it] == 0: q.append(it)
    return topo

