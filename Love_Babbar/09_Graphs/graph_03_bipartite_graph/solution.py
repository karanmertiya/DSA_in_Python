# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: BFS/DFS coloring approach. Color adjacent nodes with alternate colors (0 and 1). If an adjacent node has the SAME color, it's not bipartite.

from collections import deque
def isBipartite(graph: list[list[int]]) -> bool:
    n = len(graph)
    color = [-1] * n
    for i in range(n):
        if color[i] != -1: continue
        q = deque([i])
        color[i] = 0
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    q.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    return True

