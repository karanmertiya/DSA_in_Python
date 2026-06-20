# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: A DAG has a topological sort of exactly V elements. Use Kahn's BFS. If the number of elements pulled from the queue is < V, there's a cycle.

def isCyclic(V: int, adj: List[List[int]]) -> bool:
    indegree = [0] * V
    for i in range(V):
        for it in adj[i]: indegree[it] += 1
    q = [i for i in range(V) if indegree[i] == 0]
    cnt = 0
    while q:
        node = q.pop(0)
        cnt += 1
        for it in adj[node]:
            indegree[it] -= 1
            if indegree[it] == 0: q.append(it)
    return cnt != V

