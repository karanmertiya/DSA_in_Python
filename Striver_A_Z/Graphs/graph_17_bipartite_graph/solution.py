# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Use BFS to color the graph with 2 colors (0 and 1). Start with a node, color it 0. All its neighbors must be colored 1, their neighbors 0, and so on. If we ever find an adjacent node with the same color, the graph is not bipartite.

from collections import deque
def isBipartite(V, adj):
    color = [-1] * V
    def check(start):
        q = deque([start])
        color[start] = 0
        while q:
            node = q.popleft()
            for nbr in adj[node]:
                if color[nbr] == -1:
                    color[nbr] = 1 - color[node]
                    q.append(nbr)
                elif color[nbr] == color[node]:
                    return False
        return True
    for i in range(V):
        if color[i] == -1:
            if not check(i): return False
    return True

