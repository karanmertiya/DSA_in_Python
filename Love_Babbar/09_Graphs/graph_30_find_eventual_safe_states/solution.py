# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: Reverse all edges in the graph. Terminal nodes become sources (indegree 0). Run Kahn's algorithm (BFS topological sort). Any node processed is part of a path that only leads to terminal nodes (safe node). Sort the resulting nodes.

import collections
def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    V = len(graph)
    adjRev = [[] for _ in range(V)]
    indegree = [0] * V
    for i in range(V):
        for neighbor in graph[i]:
            adjRev[neighbor].append(i)
            indegree[i] += 1
    q = collections.deque([i for i in range(V) if indegree[i] == 0])
    safeNodes = []
    while q:
        node = q.popleft()
        safeNodes.append(node)
        for neighbor in adjRev[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return sorted(safeNodes)

