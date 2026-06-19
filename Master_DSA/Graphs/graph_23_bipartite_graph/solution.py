# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Try to color the graph using 2 colors. Use BFS/DFS. For every unvisited node, color it 0. For its neighbors, color them opposite (1). If a neighbor is already colored with the SAME color, it's not bipartite.

def isBipartite(V: int, adj: List[List[int]]) -> bool:
    color = [-1] * V
    def check(start):
        q = collections.deque([start])
        color[start] = 0
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    q.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    for i in range(V):
        if color[i] == -1:
            if not check(i): return False
    return True

